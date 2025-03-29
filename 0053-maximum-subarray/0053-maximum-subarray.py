class Solution:
    def maxSubArray(self, nums: List[int]) -> int:            
        max_value = nums[0]
        sum_value = 0

        for n in nums:
            if sum_value < 0:
                sum_value = 0

            sum_value += n
            max_value = max(max_value, sum_value)
        
        return max_value