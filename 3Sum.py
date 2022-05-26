class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=set()
        nums.sort()
        for i,k in enumerate(nums):
            l=i+1
            r=len(nums)-1
            while(l<r):
                currSum=nums[l]+nums[r]+k
                if(currSum==0):
                    output.add((k,nums[l],nums[r]))
                    l+=1
                elif(currSum<0):
                    l=l+1
                else:
                    r=r-1
        return output
        
