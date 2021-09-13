"""
leet code https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Example 4:

Input: x = 0
Output: 0

"""


class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            is_negative = ""
            x_in_list = list(str(x))
        else:
            is_negative = "-"
            x_in_list = list(str(x))[1:]
        start_index = 0
        end_index = len(x_in_list)-1
        while start_index < end_index:
            x_in_list[start_index], x_in_list[end_index] = x_in_list[end_index], x_in_list[start_index]
            end_index -= 1
            start_index += 1
        x_in_str = is_negative + ''.join(x_in_list)
        x = int(x_in_str)
        if -(2**31) < x < (2**31) -1:
            return x
        else:
            return 0


if __name__ == "__main__":
    test_cases = [
        {
            "input": 123,
            "output": 321
        },
        {
            "input": -123,
            "output": -321
        },
        {
            "input": 120,
            "output": 21
        },
        {
            "input": 0,
            "output": 0
        },
        {
            "input": 1534236469,    # case of [-231, 231 - 1] if o/p beyond this range then return 0
            "output": 0

        }
    ]
    obj = Solution()
    for test in test_cases:
        input_data = test["input"]
        out_data = test["output"]
        assert out_data == obj.reverse(input_data)
