"""
Reversing an array in place
"""


def reverse_array_in_place(arr):
    """with while loop"""
    begin_index = 0
    end_index = len(arr)-1

    while end_index > begin_index:
        arr[begin_index], arr[end_index] = arr[end_index], arr[begin_index]
        begin_index += 1
        end_index -= 1
    return arr


def reverse_array_in_place_with_for_loop(arr):
    """with for loop"""
    begin_index = 0
    end_index = len(arr)-1

    for index in range(len(arr)-1):
        if end_index > begin_index:
            arr[begin_index], arr[end_index] = arr[end_index], arr[begin_index]
            begin_index += 1
            end_index -= 1
    return arr


if __name__ == "__main__":
    input_array = [1, 2, 3, 4, 5]
    input_array = reverse_array_in_place(input_array)
    print(f"Output of array reversal using while loop {input_array}")
    input_array = reverse_array_in_place_with_for_loop(input_array)
    print(f"Output of array reversal using while loop {input_array}")



