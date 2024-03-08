class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l,count=len(s)-1,0
        while(l>=0 and s[l]==' '):
            l-=1
        while(l>=0 and s[l]!=' '):
            count+=1
            l-=1
        return count
        