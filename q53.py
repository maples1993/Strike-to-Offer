"""
Date: 2018/9/3
"""


class Solution:
    def isNumeric(self, s):
        # write code here
        if not s:
            return False

        flag_num = False
        flag_sign = False
        flag_exp = False
        flag_point = False
        for c in s:
            if ord('0') <= ord(c) <= ord('9'):
                if not flag_num:
                    flag_num = True
            elif c in ['+', '-']:
                if not flag_exp and flag_point:
                    return False

                if not flag_num and not flag_sign:
                    flag_sign = True
                else:
                    return False
            elif c in ['e', 'E']:
                if flag_num and not flag_exp:
                    flag_exp = True
                    flag_point = True
                    flag_sign = False
                    flag_num = False
                else:
                    return False
            elif c == '.':
                if not flag_point:
                    flag_point = True
                    flag_num = False
                else:
                    return False
            else:
                return False
        return flag_num