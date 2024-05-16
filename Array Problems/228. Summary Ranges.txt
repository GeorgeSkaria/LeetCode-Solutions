class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l,a,b=len(nums),0,1
        res=[]
        if (len(nums)==0):
            return res
        if (len(nums)==1):
            return [str(nums[0])]
            
        while(b<l):
            print(a,b,res)
            if(nums[b]==nums[b-1]+1):
                b+=1
            else:
                if(b-a != 1):
                    res.append(str(nums[a])+'->'+str(nums[b-1]))
                else:
                    res.append(str(nums[b-1]))
                a=b
                b+=1
        if(b-a != 1):
            res.append(str(nums[a])+'->'+str(nums[b-1]))
        else:
            res.append(str(nums[b-1]))
        return res

        