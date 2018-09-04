"""
Date: 2018/8/31
***
"""


class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        elif len(ss) == 1:
            return [ss]

        res = []
        ss = list(ss)
        for i in range(len(ss)):
            ss[0], ss[i] = ss[i], ss[0]
            collection = self.Permutation(''.join(ss[1:]))
            for item in collection:
                res.append(ss[0] + item)
            ss[0], ss[i] = ss[i], ss[0]
        res = sorted(list(set(res)))
        return res
