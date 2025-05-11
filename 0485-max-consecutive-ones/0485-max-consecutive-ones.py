class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        maxi=0
        maxconsec=0
        for i in range(n):
            if nums[i]==1:
                maxi+=1
            else:
                maxi=0
            maxconsec = max(maxconsec, maxi)
        return maxconsec
            


            