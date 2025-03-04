#Iterative division
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        val = 1
        while val <= n:
            val *= 3
        val //= 3
        while val != 0:
            while val > n:
                val //= 3
            n -= val
            val //= 3
        return n==0
#Best Solution
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 2:
                return False
            n //= 3
        return True

        
                
        
