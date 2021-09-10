"""
Interview Question #2

"A palindrome is a string that reads the same forward and backward"

For example: radar or madam

Our task is to design an optimal algorithm for checking whether a given string is palindrome or not!

"""


def reverse_string(input):
    """find reverse of a string"""
    value = ""
    for i in range(len(input)-1, -1, -1):
        value += input[i]
    return value


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
            "output": True
        },
        {
            "input": "aa",
            "output": True
        },
        {
            "input": None,
            "output": False
        },
    ]
    for test in test_cases:
        input_data = test["input"]
        if input_data not in [None, ""]:
            result = is_string_palindrome(input_data)
            print(f" Input {input_data} output {result}")
            result = is_string_palindrome_using_slicing(input_data)
            print(f" Input {input_data} output {result}")

