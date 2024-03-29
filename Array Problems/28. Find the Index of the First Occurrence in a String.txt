class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        
        return -1

#find() method can be used to solve this problem in very few lines.
 
 find(substring, start=0, end=len(string)): This method searches for the first occurrence of a substring within a string. It returns the index of the substring if found, or -1 if not found. Optionally, you can specify start and end indexes to limit the search range.