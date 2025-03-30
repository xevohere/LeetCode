class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero, one, two = 0, 0, 0
        for num in nums:
            if(num==0):
                zero+=1
            elif(num==1):
                one+=1
            else:
                two+=1
        
        i=0
        while i<zero:
            nums[i]=0
            i+=1
        while i<(one+zero):  
            nums[i]=1
            i+=1
        while i<(one+zero+two):
            nums[i]=2
            i+=1