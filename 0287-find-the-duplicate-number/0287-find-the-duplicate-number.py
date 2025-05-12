class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = len(nums)
        nums.sort()
        
        for i in range(m):
            if nums[i]==nums[i+1]:
                return nums[i]