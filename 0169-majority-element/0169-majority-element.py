class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        elmap={}
        n = len(nums)
        
        for val in nums:
            elmap[val] = elmap.get(val, 0) + 1
            
            if elmap[val]>n//2:
                return val         