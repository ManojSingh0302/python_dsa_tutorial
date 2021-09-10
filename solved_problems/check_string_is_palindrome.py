"""
Interview Question #2

"A palindrome is a string that reads the same forward and backward"

For example: radar or madam

Our task is to design an optimal algorithm for checking whether a given string is palindrome or not!

"""


def reverse_string(input_value):
    """find reverse of a string"""
    output_value = ""
    for index in range(len(input_value)-1, -1, -1):
        output_value += input_value[index]
    return output_value


def is_string_palindrome(input_string):
    """solution 1: checks if a string is palindrome"""
    reversed_string = reverse_string(input_string)
    if input_string == reversed_string:
        return True
    else:
        return False


def is_string_palindrome_using_slicing(input_string):
    """solution 2: using slicing operations"""
    is_palindrome = False
    if input_string == input_string[::-1]:
        is_palindrome = True
    return is_palindrome


if __name__ == "__main__":
    test_cases = [
        {
            "input": "madam",
            "output": True
        },
        {
            "input": "radar",
            "output": True
        },
        {
            "input": "manoj",
            "output": False
        },
        {
            "input": "car",
            "output": False
        },
        {
            "input": None,
            "output": False
        },
    ]
    for test in test_cases:
        input_data = test["input"]
        out_data = test["output"]
        if input_data not in [None, ""]:
            assert is_string_palindrome(input_data) == out_data, f"Test case failed for input {input_data}"
            assert is_string_palindrome_using_slicing(input_data) == out_data, f"Test case failed for input {input_data}"

