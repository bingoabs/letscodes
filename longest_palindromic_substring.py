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

class Solution(object):

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

    def longestPalindrome(self, string):

        sets = set(string)
        if len(sets) == len(string): return string[0:1]
        if len(sets) <= 1: return string

        letters = {}
        for i in sets: letters[i] = 0

        for i in string: letters[i] += 1

        unique, double = "", ""

        for key, value in letters.items():
            if value == 1:
                unique = key
            if value == 2:
                double = key
                break
        if unique:
            splited_list = string.split(unique)
            head, end = splited_list[0], splited_list[-1]
            f_head, f_end = self.get_same(head, end)
            preresult = f_head + unique + f_end

            head_result, end_result = "", ""

            if len(preresult) < len(head):
                head_result = self.longestPalindrome(head)

            if len(preresult) < len(end):
                end_result = self.longestPalindrome(end)

            result = head_result if len(head_result) > len(end_result) else end_result
            result = preresult if len(preresult) > len(result) else result

        elif double:
            splited_list = string.split(double)
            head, middle, end = splited_list[0], splited_list[1], splited_list[2]
            list_middle = list(middle)
            list_middle.reverse()
            preresult = ""
            if list_middle == list(middle):
                f_head, f_end = self.get_same(head, end)
                preresult = f_head + double + middle + double + f_end

            head_result, end_result = "", ""
            big_head = head + double + middle
            if len(preresult) < len(big_head):
                head_result = self.longestPalindrome(big_head)
            big_end = middle + double + end
            if len(preresult) < len(big_end):
                end_result = self.longestPalindrome(big_end)
            result = head_result if len(head_result) > len(end_result) else end_result
            result = preresult if len(preresult) > len(result) else result


        return result

    def get_same(self, head, end):
        head = list(head)
        head.reverse()
        same_part = []
        length = min(len(head), len(end))
        for i in range(length):
            if head[i] != end[i]:
                break
            same_part.append(head[i])
        from_end = "".join(same_part)
        same_part.reverse()
        from_head = "".join(same_part)
        return from_head, from_end

if __name__ == "__main__":
    s = "abcbe"
    r = Solution().longestPalindrome(s)
    print r


