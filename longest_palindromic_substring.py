"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example:

Input: "cbbd"
Output: "bb"

"""

# class Solution(object):

    # def validate_palindromic(self, string):
    #     reverse = list(string)
    #     reverse.reverse()
    #     return True if reverse == list(string) else False

    # def get_longest_with_start(self, start, offset):
    #     letter = self.string[start]
    #     for i in range(start + 1, self.length):
    #         if self.string[i] == letter:
    #             if i - start > offset and self.validate_palindromic(self.string[start: i+1]):
    #                 offset = i - start

    #     return start, offset

    # def _longestPalindrome(self, s):
        # Use the directly way, depend on the ability of the computer...
        # :type s: str
        # :rtype: str
        # notice, can first set the string, get the basic info about the string,
        # then to more precise to do next step..
        # self.string = s
        # self.length = len(s)

        # start = 0
        # offset = 0
        # substring = ""
        # while self.length - start > offset + 1:
        #     start, new_offset = self.get_longest_with_start(start, offset)
        #     if new_offset > offset:
        #         offset = new_offset
        #         substring = s[start:start + offset + 1]
        #         print("start: {}; offset: {}; substring: {}".format(start, offset, substring))
        #     start += 1
        # if substring == "":
        #     return s[0]
        # return substring

# class Solution(object):
    # another way to count, little better than last one which using violent crack way...
    # def validate_palindromic(self, string):
    #     reverse = list(string)
    #     reverse.reverse()
    #     return True if reverse == list(string) else False

    # def get_longest(self, string, start, offset):
    #     length = len(string)
    #     letter = string[start]
    #     new_offset = offset
    #     for i in range(start + offset + 1, length):
    #         if string[i] == letter:
    #             target = string[start: i+1]
    #             if self.validate_palindromic(target):
    #                 new_offset = i - start

    #     return start, new_offset

    # def loop(self, string):
    #     length = len(string)
    #     start, offset = 0, 0
    #     while length - start > offset + 1:
    #         start, new_offset = self.get_longest(string, start, offset)
    #         if new_offset > offset:
    #             offset = new_offset
    #             substring = string[start:start + offset + 1]
    #             print("start: {}; offset: {}; substring: {}".format(start, offset, substring))
    #         start += 1
    #     return substring
import time

# class Solution(object):
#     # a little better way to improve the property of finding longest palindrome string.
#     def get_middle(self, number):
#         return number/2*2 - number

#     def get_same(self, head, end):
#         head = list(head)
#         head.reverse()
#         same_part = []
#         length = min(len(head), len(end))
#         for i in range(length):
#             if head[i] != end[i]:
#                 break
#             same_part.append(head[i])
#         from_end = "".join(same_part)
#         same_part.reverse()
#         from_head = "".join(same_part)
#         return from_head, from_end

#     def longestPalindrome(self, string):
#         print("")
#         sets = set(string)
#         if len(sets) == len(string): return string[0:1]
#         if len(sets) <= 1: return string

#         letters = {}
#         for i in sets: letters[i] = 0

#         for i in string: letters[i] += 1

#         odd, even, half = "", "", 0
#         print(letters)
#         for key, value in letters.items():
#             no = self.get_middle(value)
#             if value == 1:
#                 odd, half = key, 0
#                 break
#             if no == 0:
#                 even, half = key, value/2
#                 break
#             if no == -1:
#                 odd, half = key, value/2
#                 break
#         print("string: {}; odd: {}; even: {}; half: {}".format(string, odd, even, half))

#         if odd:
#             count = 0
#             for i in range(len(string)):
#                 if string[i] == odd:
#                     count +=1
#                 if count == half + 1:
#                     index = i
#                     break

#             head, end = string[0:index], string[index+1:]
#             print("odd: {};index: {}; head:{}: end: {}".format(odd, index, head, end))
#             f_head, f_end = self.get_same(head, end)
#             preresult = f_head + odd + f_end

#             head_result, end_result = "", ""

#             if len(preresult) < len(head):
#                 head_result = self.longestPalindrome(head)

#             if len(preresult) < len(end):
#                 end_result = self.longestPalindrome(end)

#             result = head_result if len(head_result) > len(end_result) else end_result
#             result = preresult if len(preresult) > len(result) else result

#         elif even:
#             count = 0
#             for i in range(len(string)):
#                 if string[i] == even:
#                     count += 1
#                     print("letter: {}; i: {}; count: {}".format(string[i], i, count))
#                     if count == half:
#                         index1 = i
#                     if count == half + 1:
#                         index2 = i
#                         break
#             head, middle, end = string[:index1], string[index1+1:index2], string[index2+1:]
#             print("string: {}; even: {};index1: {}; index2: {}; head: {}; middle:{}: end: {}".format(string, even, index1, index2, head, middle, end))

#             list_middle = list(middle)
#             list_middle.reverse()
#             preresult = ""
#             if list_middle == list(middle):
#                 f_head, f_end = self.get_same(head, end)
#                 preresult = f_head + even + middle + even + f_end

#             head_result, end_result = "", ""
#             big_head = head + even + middle
#             if len(preresult) < len(big_head):
#                 head_result = self.longestPalindrome(big_head)
#             big_end = middle + even + end
#             if len(preresult) < len(big_end):
#                 end_result = self.longestPalindrome(big_end)
#             result = head_result if len(head_result) > len(end_result) else end_result
#             result = preresult if len(preresult) > len(result) else result
#         else:
#             #when search "babadada", still need regular way to do...


#         return result


class Solution(object):
    def longestPalindrome(self, string):

        sets = set(string)
        length = len(string)

        if len(sets) == length: return string[0:1]
        if len(sets) <= 1: return string

        letters = {}
        for i in sets: letters[i] = 0

        for i in string: letters[i] += 1

        index, target = 0, ""

        max_index = length -1

        while max_index - index >= len(target):
            result = self.do_check(string[index:], target)
            if len(target) < len(result):
                target = result
            index += 1
        return target

    def do_check(self, string, target):
        longest = len(target)
        letter, length = string[0], len(string)

        reverse = list(string)
        reverse.reverse()

        index, max_index = 0, length - 1
        new_target = ""

        while max_index - index >= len(target):
            if reverse[index] == letter:
                part = reverse[index:]
                part.reverse()
                if reverse[index:] == part:
                    new_target = part
                    break

            index += 1

        if len(new_target) > longest:
            return "".join(new_target)
        else:
            return target






if __name__ == "__main__":
    s = "abb"
    r = Solution().longestPalindrome(s)
    print r







