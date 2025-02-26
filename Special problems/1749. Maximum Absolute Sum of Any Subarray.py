class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        presum = 0
        maxpre,minpre = 0,0

        for i in nums:
            presum += i
            maxpre = max(maxpre,presum)
            minpre = min(minpre,presum)
        
        return maxpre - minpre
        
        

  '''To maximize the absolute subarray sum, we need to find two prefix sums — one that is as large as possible 
  and another that is as small as possible. This is because the sum of any subarray between indices i and j can
  be expressed as prefixSum[j] - prefixSum[i]. The greater the difference between prefixSum[j] and prefixSum[i],
  the larger the absolute sum of the subarray. Thus, to maximize this difference, prefixSum[j] should be as large
  as possible, while prefixSum[i] should be as small as possible.'''
