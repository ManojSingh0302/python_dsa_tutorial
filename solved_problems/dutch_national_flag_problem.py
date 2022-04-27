"""
The problem is that we want to sort a T[] one-dimensional array of integers in O(N) running time - and without any
extra memory. The array can contain values: 0, 1 and 2 (check out the theoretical section for further information).

"""


def dutch_flag_problem(input_num_array, mid=1):
    i, j = 0, 0
    k = len(input_num_array) - 1

    while j <= k:
        if input_num_array[j] < mid:  # here the the value at position j will 0
            input_num_array[i], input_num_array[j] = input_num_array[j], input_num_array[i]
            i += 1
            j += 1

        elif input_num_array[j] > mid:  # here the the value at position j will 2
            input_num_array[j], input_num_array[k] = input_num_array[k], input_num_array[j]
            k = k - 1

        else:  # here the the value at position j will 1
            j += 1
    return input_num_array


if __name__ == "__main__":
    num_array = [0, 1, 2, 1, 2, 0, 0]
    num_array = dutch_flag_problem(num_array)
    print("Sorted array", num_array)
