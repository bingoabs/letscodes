"""
This is the simple way to mask the sensitive message
In real world, need first ensure the `string` is email string or phone number string
"""
class Solution(object):
    def maskPII(self, S):
        if "@" in S:#email
            first, after = S.split("@")
            return "{}*****{}@{}".format(
                first[0], first[-1], after).lower()

        else:
            digits = filter(unicode.isdigit, S)
            local = "***_***-{}".format(digits[-4:])
            if len(digits) == 10:
                return local
            return "+{}-".format("*" * (len(digits) - 10)) + local

import re

def extract_phone_numbers(string):
    """
    When sure the result is email, then mask the email and replace the raw string
    """
    return re.findall(r"\w+@\w+\.\w+", string)

def extract_emails(string):
    """
    When sure the result is phone number, then mask the ohone number and replace the raw string
    """
    return re.findall(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]", text)


