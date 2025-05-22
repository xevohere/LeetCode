class Solution:
    def trap(self, height: List[int]) -> int:
        
        #we need to get the leftmax and rightmax lists first

        leftmax=[0]*len(height)
        leftmax[0] = height[0]
        for i in range(1, len(height)):
            if height[i]>leftmax[i-1]:
                leftmax[i]=height[i]
            else:
                leftmax[i]=leftmax[i-1]
        
        rightmax=[0]*len(height)
        rightmax[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            if height[i]>rightmax[i+1]:
                rightmax[i] = height[i]
            else:
                rightmax[i] = rightmax[i+1]


        total_water = 0
        for i in range(len(height)):
            total_water += abs(min(leftmax[i], rightmax[i]) - height[i])
        return total_water
    
    