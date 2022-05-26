class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freqMap={}
        for i,k in enumerate(nums):
            diffValue=(target-k)
            if (diffValue in freqMap):
                return (freqMap[diffValue],i)
            else:
                freqMap[k]=i
        
