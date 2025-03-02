class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for i,j in nums1:
            d[i] += j
        for i,j in nums2:
            d[i] += j
        
        return sorted([[i,j] for i,j in d.items()])

        
