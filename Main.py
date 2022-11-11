from SubPkg.StringConversation import *
from SubPkg.LookUpTableClass import *
from SubPkg.BitStringFoos import *
from SubPkg.ArrayShiftClass import *


class Crypt(object):
    def __init__(self, password, data, cycles=6):
        self.Gen = KeyGen(password)
        self.cycles = cycles
        self.table = KeyTable(self.Gen.key)
        self.key_arr = bitstring_to_bytes(self.Gen.key)
        self.key_instance = self.key_arr[0]
        self.blocks = yield_blocks(string_to_bytes(data))
        self.ShiftFoo = ShiftArray
        self.XorFoo = XOR
        self.key_iteration = 0

    def key_morph(self):
        self.key_iteration += 1
        if self.key_iteration == len(self.key_arr):
            self.key_iteration = 0
        self.key_instance = self.XorFoo((self.key_arr[self.key_iteration], self.key_instance))


class Decrypt(Crypt):
    def __init__(self, key, data):
        super().__init__(key, data)

    def cycle(self, block):
        shift = self.ShiftFoo(block)
        shift.shift_in_cycle()
        block = shift.array
        for row in range(len(block)):
            for col in range(len(block[row])):

                block[row][col] = self.table.lookup(self.XorFoo((block[row][col], self.key_instance)))
        return block

    def decrypt(self):
        output = ''
        for block in self.blocks:
            self.key_morph()
            for cycle in range(self.cycles):
                block = self.cycle(block)
            output += stringify_blocks(block)
        return output


class Encrypt(Crypt):
    def __init__(self, key, data):
        super().__init__(key, data)
        self.blocks = yield_blocks(bitstring_to_bytes(data))

    def cycle(self, block):
        for row in range(len(block)):
            for col in range(len(block[row])):
                block[row][col] = self.XorFoo((self.table.lookup(block[row][col], reverse=True), self.key_instance))
        shift = self.ShiftFoo(block)
        shift.shift_out_cycle()
        block = shift.array
        return block

    def encrypt(self):
        output = ''
        for block in self.blocks:
            self.key_morph()
            for cycle in range(self.cycles):
                block = self.cycle(block)
            for row in block:
                output += byteArr_to_string(row)
        return output


text = 'Hello World. Let´s decrypt your message!'

if __name__ == '__main__':
    de = Decrypt('RazeVortex', text)
    decrypted = de.decrypt()
    print('decrypted:')
    print(decrypted)
    en = Encrypt('RazeVortex', decrypted)
    print('encrypted:')
    print(en.encrypt())
