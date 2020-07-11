class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
        return nums
Space complexity- O(n) and time- O(n)
 
 
 class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        for j in range(n):
            if nums[j]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
 Space- O(1) and Time- O(n)
 
