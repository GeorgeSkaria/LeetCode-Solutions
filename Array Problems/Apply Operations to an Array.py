class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        stack = [nums[0]]

        for i in range(1,len(nums)):
            if nums[i] == stack[-1]:
                stack[-1] *= 2
                nums[i] = 0
            stack.append(nums[i])

        i,j = 0,1
        while (j < len(nums)):
            if stack[i] != 0:
                i += 1
            if stack[j] != 0:
                stack[i],stack[j] = stack[j],stack[i]
            j += 1
        return stack
        
