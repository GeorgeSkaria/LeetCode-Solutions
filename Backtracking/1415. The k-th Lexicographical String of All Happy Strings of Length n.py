"""
Problem: Find the k-th lexicographically smallest happy string of length n.
A happy string is a string consisting of 'a', 'b', and 'c' where no two adjacent characters are the same.
"""

class Solution:
    # Backtracking Solution
    def getHappyString_backtrack(self, n: int, k: int) -> str:
        res = []
        letters = ['a', 'b', 'c']

        def backtrack(s):
            if len(s) == n:
                res.append(s)
                return
            for letter in letters:
                if not s or s[-1] != letter:
                    backtrack(s + letter)

        backtrack("")
        return res[k-1] if len(res) >= k else ""

    # Iterative Optimized Solution
    def getHappyString_iterative(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        total = 2 ** (n - 1)

        if k > 3 * total:
            return ""

        result = []
        prev = ''
        k -= 1 

        for i in range(n):
            for letter in letters:
                if letter != prev:
                    if k < total:
                        result.append(letter)
                        prev = letter
                        break
                    k -= total
            total //= 2
        
        return "".join(result)

    '''Time O(n)
       Space O(1)
    '''


