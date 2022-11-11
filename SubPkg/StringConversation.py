if __name__ == '__main__':
    from BitStringFoos import int_to_bitString as to_bit, bit_to_int as to_int
else:
    from SubPkg.BitStringFoos import int_to_bitString as to_bit, bit_to_int as to_int


def string_to_bytes(string):
    byte_arr = [to_bit(ord(char), bit_size=256) for char in string]
    full_block = 16 % len(byte_arr)
    for i in range(full_block):
        byte_arr.append(to_bit(0, bit_size=256))
    return byte_arr


def byteArr_to_string(arr):
    string = ''
    for char in arr:
        if to_int(char) != 0:
            string += chr(to_int(char))
    return string


def yield_blocks(arr, block_lenght=16, row_lenght=4):
    for block in range(len(arr) // block_lenght):
        x = block * block_lenght
        t_strip = arr[x:x + block_lenght]
        t_arr = []
        for row in range(row_lenght):
            y = row * row_lenght
            t_arr.append(t_strip[y:y + row_lenght])
        yield t_arr


def stringify_blocks(arr):
    string = ''
    for row in arr:
        for col in row:
            string += col
    return string


def bitstring_to_bytes(string):
    return [string[byte * 8:byte * 8 + 8] for byte in range(len(string) // 8)]


if __name__ == '__main__':
    blocks = yield_blocks(string_to_bytes('Hello World. What´s up with you today?'))
    #print(len(string_to_bytes('Hello World.')))
    #print(byteArr_to_string(string_to_bytes('Hello World.')))
    string = ''
    for block in blocks:
        string += stringify_blocks(block)
    print(bitstring_to_bytes(string))
