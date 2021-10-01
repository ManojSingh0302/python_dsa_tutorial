"""
Find the uniques set of two elements from the given list where addition of two elements is equal to the sum value.

eg:
input:
    number_list = [1,2,4,3,3,5,5,5,7,8]
    sum = 8

output
    [(1,7),(3,5)]

"""


# solution 1
def get_two_sum(arr, sum):
    result_dict = {}
    output = []
    for index, element in enumerate(arr):
        for j in range(index + 1, len(arr) - 1):
            if sum == (element + arr[j]):
                result_dict[element] = arr[j]
                to_store = element, arr[j]
                if to_store not in output:
                    output.append(to_store)

    return output


if __name__ == "__main__":
    test_cases = [
        {
            "input_1": [1, 2, 4, 3, 3, 5, 5, 5, 7, 8],
            "input_2": 8,
            "output": [(1, 7), (3, 5)]
        }
    ]
    for test in test_cases:
        input_data_1 = test["input_1"]
        input_data_2 = test["input_2"]
        out_data = test["output"]
        assert out_data == get_two_sum(input_data_1, input_data_2)
