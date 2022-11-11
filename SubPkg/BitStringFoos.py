# valid_string is only used to check if a string can be interpreted as a binary input means only contains 0 and 1 values
def valid_string(bit_string):
    if type(bit_string) == tuple:
        t_string = ''
        for string in bit_string:
            t_string += string
    else:
        t_string = bit_string
    for char in t_string:
        if char in '01':
            pass
        else:
            print('invalid string')
            return False
    return True


def XOR(strings: tuple):
    t_string = ''
    if valid_string(strings) and len(strings[0]) == len(strings[1]):
        for i in range(len(strings[0])):
            if strings[0][i] == strings[1][i]:
                t_string += '0'
            else:
                t_string += '1'
    return t_string


def int_to_bitString(integer, bit_size=16):
    bit_size /= 2
    t_string = ''
    while True:
        t_string += str(int(integer / bit_size))
        integer = integer % bit_size
        if bit_size == 1:
            return t_string
        bit_size = bit_size / 2


def tuple_to_bitString(integer:tuple, bit_size=16):
    t_string = ''
    for val in integer:
        t_string += int_to_bitString(val, bit_size=bit_size)
    return t_string


def bit_to_int(string):
    if valid_string(string):
        string = string[::-1]
        value = 0
        for i in range(len(string)):
            if string[i] == '1':
                if i == 0:
                    value += 1
                else:
                    value += 2 ** i
        return value
    else:
        return False


def split_bit(string):
    if valid_string(string):
        return (bit_to_int(string[0:4]), bit_to_int(string[4:]))
    else:
        return False

# Hex isn´t used so far
'''
HEX = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')


def to_Hex(string):
    int_pair = split_bit(string)
    return f'{HEX[int_pair[0]]}{HEX[int_pair[1]]}'
'''

if __name__ == '__main__':
    string = '00001111'
    print(bit_to_int(string))
    print(split_bit(string))