from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_element = Counter(nums)
        ls = []
        n = len(nums)
        for element , value in count_element.items():
            if value > n/3:
                ls.append(element)
        return ls
        