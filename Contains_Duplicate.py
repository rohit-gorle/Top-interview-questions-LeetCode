class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       
        result = set(nums)
        if len(result)==len(nums):
            return 0
        return 1
       
       
       
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       
        result = {}
        for i in nums:
            if i in result:
                return 1
            else:
                result[i]=0
        return 0       
