class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sums = 0
        
        result = nums[0]
        for i in range(0,len(nums)):
            sums = nums[i]
            for j in range(i+1,len(nums)):
                sums += nums[j]
                result = max(result,sums,nums[i])
        return max(result,sums)  
        
        
1st solution- using brute force approach - time limit exceeded



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i],nums[i])
        return max(nums)  

2nd solution using max of previous plus present, present. without using any extra space allocation





class Solution: 
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)
        
        
        
3rd solution using dp and creating new dp array.        
