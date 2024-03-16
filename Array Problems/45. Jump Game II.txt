class Solution:
    def jump(self, nums: List[int]) -> int:
        jum,i=0,0
        l=len(nums)-1
        while(i!=l):
            if(i+nums[i]>=l):
                jum+=1
                l=i
                i=0
            else:
                i+=1
        return jum



 #GREEDY APPROACH
	
1)Initialize variables jum and i to 0.
2)Find the last index of the array, denoted by l.
3)If the sum of the current index i and its corresponding jump value nums[i] can reach or exceed the last index l, then it means that a jump from the current index can reach the end of the array. In this case, we increment jum to indicate a jump, set the last index l to the current index i, and reset i to 0 to start from the beginning of the array again.
4)If the current index i does not lead to reaching the end of the array, increment i by 1 to consider the next index.
