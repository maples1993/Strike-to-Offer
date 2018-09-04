"""
Date: 2018/9/1
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1

        alphabet = {}
        for x in s:
            if x not in alphabet:
                alphabet[x] = 1
            else:
                alphabet[x] += 1
        for i, x in enumerate(s):
            if alphabet[x] == 1:
                return i
        return -1