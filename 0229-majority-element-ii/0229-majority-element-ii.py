class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        arr = []
        hashmap = {}

        for val in nums:
            if val in hashmap:
                count = hashmap.get(val)
                count+=1
            else:
                count = 1
            hashmap[val]=count
        
        for val in hashmap:
            count = hashmap.get(val)
            if count>n//3:
                arr.append(val)
        return arr

            
