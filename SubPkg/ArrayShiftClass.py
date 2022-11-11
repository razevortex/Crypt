class ShiftArray(object):
    def __init__(self, arr):
        if self.check_array_size(arr):
            self.array = arr

    def check_array_size(self, arr):
        length = len(arr)
        for row in arr:
            if len(row) == length:
                pass
            else:
                print('size error')
                return False
        return True

    def shift_row(self, row, shift_for):
        t_arr = self.array[row]
        t_arr_size = len(t_arr)
        t_arr = self.shifting(t_arr, shift_for)
        self.array[row] = t_arr[0:t_arr_size]

    def shift_column(self, column, shift_for):
        t_arr = [row[column] for row in self.array]
        t_arr = self.shifting(t_arr, shift_for)
        for row in range(len(self.array)):
            self.array[row][column] = t_arr[row]

    def shifting(self, t_arr, shift_for):
        t_arr_size = len(t_arr)
        for _ in range(shift_for):
            subset = t_arr[t_arr_size - 1:t_arr_size]
            t_arr[0:0] = subset
        return t_arr

    def shift_in_cycle(self):
        t_arr_size = len(self.array)
        for i in range(t_arr_size):
            self.shift_row(i, i + 1)
            self.shift_column(i, i + 1)

    def shift_out_cycle(self):
        t_arr_size = len(self.array)
        for i in range(t_arr_size):
            x = t_arr_size - i - 1
            self.shift_column(x, i)
            self.shift_row(x, i)

    def print_array(self):
        [print(row) for row in self.array]
        print('')


if __name__ == '__main__':
    arr = []
    for i in range(4):
        row = []
        for ii in range(4):
            x = i * 4
            row.append(x + ii)
        arr.append(row)
    [print(row) for row in arr]

    test = ShiftArray(arr)
    test.shift_in_cycle()
    test.print_array()
    test.shift_out_cycle()
    test.print_array()
