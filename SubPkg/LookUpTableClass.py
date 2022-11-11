from random import seed, randint as rng
from SubPkg.BitStringFoos import int_to_bitString as to_bit, split_bit, tuple_to_bitString as join_int


class KeyGen(object):
    def __init__(self, password):
        self.key = ''
        self.generator(self.grow_seed(password))

    def grow_seed(self, password):
        string_seed_num = ''
        for char in password:
            string_seed_num += str(ord(char))
        return int(string_seed_num)

    def generator(self, seed_val):
        t_arr = []
        seed(seed_val)
        for i in range(16):
            for row in range(16):
                t = rng(0, 255)
                while t in t_arr:
                    t = rng(0, 255)
                t_arr.append(t)
                self.key += to_bit(t, bit_size=256)


class KeyTable(object):
    def __init__(self, key):
        t_arr = self.split_key(key)
        self.table = []
        for x in range(16):
            t_row = []
            for y in range(16):
                i = x + 16 * y
                t_row.append(t_arr[i])
            self.table.append(t_row)

    def split_key(self, key):
        t_arr = []
        for i in range(256):
            x = i * 8
            t_arr.append(key[x:x + 8])
        return t_arr

    def get_index(self, string):
        for x in range(len(self.table)):
            if string in self.table[x]:
                return join_int((x, self.table[x].index(string)))

    def get_value(self, string):
        index_tuple = split_bit(string)
        return self.table[index_tuple[0]][index_tuple[1]]

    def lookup(self, string, reverse=False):
        if reverse:
            return self.get_index(string)
        else:
            return self.get_value(string)


if __name__ == '__main__':
    gen = KeyGen('test key gen')
    print(gen.key)
