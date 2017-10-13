#/usr/bin/env python

# Regular Expression Matching

"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char*p)

Some examples:
isMatch('aa', 'a') -> false
isMatch('aa', 'aa') -> true
isMatch('aaa', 'aa') -> false
isMatch('aa', 'a*') -> true
isMatch('aa', '.*') -> true∏
isMatch("ab", ".*") -> true
isMatch("aab", "c*a*b") -> true

maybe another way to do:
    split the target string and goal string, find the match start and check the consistency with the left part
    in fact, exactly same with the current method, but due tu the spilited, left work is just to compare, 
    do not need to splite again and again...

    first try solve the problem by opposite direction, so ...
"""
# import logging

# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         if ".*" in p or s in p: return True 

#         if len(s) == 0: return True
#         if len(p) == 0: return False

#         start = s[0]

#         for i in range(len(p)):
#             if p[i] in [start, "."]:
#                 is_match = self.check(s, p[i:])
#                 if is_match: return True
#         return False

#     def check(self, s, p):
#         print(" s: {}; p: {}".format(s, p))
#         if len(s) == 0: return True
#         if len(p) == 0: return False

#         if "*" in p:
#             pre, last = p.split("*", 1)
#             if self.same(pre, s[:len(pre)]):
#                 left = self.subtract(s[len(pre):], pre[-1])
#                 print("left: {}".format(left))
#                 return self.check(left, last)
#             else:
#                 return False
#         else:
#             return self.same(s, p)

#     def subtract(self, subtracted, subtraction):
#         print("subtracted: {}; subtraction: {}".format(subtracted, subtraction))
#         for i in range(len(subtracted)):
#             if subtracted[i] != subtraction:
#                 break
#         return subtracted[i+1:]


#     def same(self, expression, string):
#         if len(string) < len(expression):return False
#         for index in range(len(expression)):
#             if expression[index] != string[index] and expression[index] != ".":
#                 return False
#         return True

class Solution(object):
    def isMatch(self, s, p):
        if len(s) == 0: return True
        if len(p) == 0: return False
        s_list = self.split(s)
        p_list = self.split(p, re=True)
        return self.comps(s_list, p_list)

    def split(self, s, re=False):
        last, part, result = s[0], '', []
        index, m_index = 0, len(s) - 1
        while re == False and index <= m_index:
            c_word = s[index]
            if c_word == last:
                part += c_word
            else:
                result.append(part)
                part = c_word
                last = c_word
            index +=1 

        while re and index <= m_index:
            c_word = s[index]
            if c_word == last or c_word == "*":
                part += c_word
            else:
                result.append(part)
                part = c_word
                last = c_word
            index += 1
        result.append(part)

        return result

    def comps(self, sl, pl):
        print("comps sl: {}; pl: {}".format(sl, pl))
        start = sl[0]
        for index in range(len(pl)):
            if pl[index] in [start, ".", ".*"] or pl[index][0:1] == start[0]:
                if self.comp(sl, pl[index:]):
                    return True
        return False

    def comp(self, sl, pl):
        print("comp sl: {}; pl: {}".format(sl, pl))
        if sl == pl: return True
        if len(sl) == 0: return True
        if len(pl) == 0: return False
        start = pl[0]
        if start == ".*":
            return self.end_with(sl, pl[1:])
        else:
            # start = "." or start == pl[0]
            return self.comp(sl[1:], pl[1:])

    def end_with(self, sl, left):
        s = "".join(sl)
        left = "".join(left)
        return s.endswith(left)

def test_split():
    s = Solution()
    print(s.split("ab"))
    print(s.split(".*c", True))
    # ['a', 'b']
    # ['.*', 'c']

if __name__ == "__main__":
    # s, p = "ab", ".*c"
    s, p = "aa", "a"
    s = Solution().isMatch(s, p)
    print(s)

    # test_split()



