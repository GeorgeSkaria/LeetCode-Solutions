1)Using Dictionary

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target)!=len(arr):
            return False
        t=Counter(target)
        a=Counter(arr)
        for k,v in a.items():
            if k in t and v==t[k]:
                continue
            return False
        return True

        
     

2)Using Sorting

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(arr)==sorted(target)

        
        
