"""
Date: 2018/9/1
"""


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n == 0:
            return 0
        elif n < 10:
            return 1

        count = 0
        num_str = str(n)
        pivot = int(num_str[0]) * 10 ** (len(num_str) - 1)

        count += self.NumberOf1Between1AndN_Solution(pivot - 1)
        if num_str[0] == '1':
            count += n - pivot + 1
        count += self.NumberOf1Between1AndN_Solution(n - pivot)

        return count


if __name__ == '__main__':
    s = Solution()
    print(s.NumberOf1Between1AndN_Solution(13))