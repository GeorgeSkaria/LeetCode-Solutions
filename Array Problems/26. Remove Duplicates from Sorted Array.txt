class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        ele=1000
        for i in range(len(nums)):
            if(nums[i]!=ele):
                ele=nums[i]
                nums[k],nums[i]=nums[i],nums[k]
                k+=1
        return k