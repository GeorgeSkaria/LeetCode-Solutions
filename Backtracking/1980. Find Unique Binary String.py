class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(nums)
        n = len(nums)
        res = [""]

        def bt(word):
            if len(word) == n:
                if word not in s:
                    res[0] = word
                return 
            
            for bit in '01':
                bt(word + bit)
                if res[0]:
                    return res[0]
        return bt("")


# To generate all missing binary strings:
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(nums)
        n = len(nums)
        res = []

        def bt(word):
            if len(word) == n:
                if word not in s:
                    res.append(word)
                return
            
            for bit in '01':
                bt(word + bit)

        bt("")
        return res
