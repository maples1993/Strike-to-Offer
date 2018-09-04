"""
Date: 2018/8/31
***
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False

        stack = []
        i1 = i2 = 0
        while stack or i2 < len(popV):
            if not stack or stack[-1] != popV[i2]:
                if i1 < len(pushV):
                    stack.append(pushV[i1])
                    i1 += 1
                else:
                    return False
            elif stack[-1] == popV[i2]:
                stack.pop(-1)
                i2 += 1
        return not stack


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = [4, 5, 3, 2, 3]
    s = Solution()
    print(s.IsPopOrder(a, b))
