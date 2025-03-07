class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = []

        def sieve(n):
            isprime = [1]*(n+1)
            isprime[0],isprime[1] = 0,0

            for i in range(2,n+1):
                if isprime[i]:
                    if i >= left:
                        prime.append(i)
                    for j in range(i*i,n+1,i):
                        isprime[j] = 0
        
        sieve(right)

        a,b = -1,-1
        minval = float('inf')
        for i in range(1,len(prime)):
            if prime[i]-prime[i-1] < minval:
                minval = prime[i] - prime[i-1]
                a,b = prime[i-1],prime[i]
        
        return [a,b]



        
