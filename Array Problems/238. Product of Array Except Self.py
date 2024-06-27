class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize two arrays to store the product of elements to the left and right of each index.
        left_products = [1] * n
        right_products = [1] * n
        
        # Calculate the product of elements to the left of each index.
        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]
        
        # Calculate the product of elements to the right of each index.
        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
        
        # Calculate the final result by multiplying left_products and right_products for each index.
        result = [left_products[i] * right_products[i] for i in range(n)]
        
        return result
