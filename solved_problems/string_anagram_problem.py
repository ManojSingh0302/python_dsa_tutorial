"""
Construct an algorithm to check whether two words (or phrases) are anagrams or not!

"An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once"

For example: restful and fluster

"""


def is_string_anagram(input_str_1, input_str_2):
    """" this take two input and returns True is strings are anagram else returns False"""

    # if two string are not of same length then they will not be anagram
    if len(input_str_1) != len(input_str_2):
        return False

    # sorting will take O(NlogN)
    input_str_1 = sorted(input_str_1)
    input_str_2 = sorted(input_str_2)

    # this will take O(N)
    for i in range(len(input_str_1) - 1):
        if input_str_1[i] != input_str_2[i]:
            return False

    # Final complexity O(NlogN) as O(NlogN) + O(N) = O(NlogN)

    return True


if __name__ == "__main__":
    print(is_string_anagram("restful", "fluster"))




