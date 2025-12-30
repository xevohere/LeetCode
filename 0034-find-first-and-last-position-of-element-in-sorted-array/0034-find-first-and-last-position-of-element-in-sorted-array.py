class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def lower_bound(nums,target):
            low,high=0,len(nums)-1
            p = high-low+1
    
            while low<=high:
                mid=(low+high)//2
        
                if nums[mid]>=target:
                    p=mid
                    high = mid-1
            
                else:
                    low = mid+1
            return p


        def upper_bound(nums,target):
            low,high=0,len(nums)-1
            q = high-low+1
    
            while low<=high:
                mid=(low+high)//2
        
                if nums[mid]>target:
                    q=mid
                    high = mid-1
            
                else:
                    low = mid+1
            return q


        lb=lower_bound(nums,target)
        ub=upper_bound(nums,target)

        if lb==len(nums) or nums[lb]!=target:
            return [-1,-1]
        return [lb, ub-1]