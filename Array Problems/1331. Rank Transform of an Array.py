class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        s = sorted(arr)
        d = {s[0]:1}
        res,r = [],2
        for i in range(1,len(s)):
            if s[i] not in d:
                d[s[i]] = r
                r += 1
        for i in arr:
            res.append(d[i])
        return res
                



        
