class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        arr = colors + colors[:-1]
        res = 0
        count = 1 

        for i in range(1, len(colors)+k-1):
            if arr[i] != arr[i - 1]:
                count += 1
            else:
                count = 1  
            
            if count >= k:
                res += 1

        return res

