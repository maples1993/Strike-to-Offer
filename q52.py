"""
Date: 2018/9/3
"""


class Solution:
    def process(self, s, pattern):
        if not s and not pattern:   # 匹配完成
            return True
        if s and not pattern:       # 有多余字符
            return False

        # 处理'.'和字符
        if len(pattern) == 1 or pattern[1] != '*':
            if s and pattern[0] == '.' or s and s[0] == pattern[0]:
                return self.process(s[1:], pattern[1:])

        # 处理'*'
        if len(pattern) > 1 and pattern[1] == '*':
            if s and pattern[0] == '.' or s and s[0] == pattern[0]:
                return self.process(s[1:], pattern[2:]) \
                       or self.process(s, pattern[2:]) \
                       or self.process(s[1:], pattern)
            else:
                return self.process(s, pattern[2:])

    def match(self, s, pattern):
        # write code here
        s = list(s)
        pattern = list(pattern)

        return self.process(s, pattern)
