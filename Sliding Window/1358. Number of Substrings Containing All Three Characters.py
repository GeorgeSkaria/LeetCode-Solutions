class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {'a':0,'b':0,'c':0}
        l = len(s)
        i,j = 0,0 
        res = 0

        while j<l:
            d[s[j]] += 1
            while d['a'] and d['b'] and d['c']:
                res += (l-j)
                d[s[i]] -= 1
                i += 1
            j += 1
        return res


        
