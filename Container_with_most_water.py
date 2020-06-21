class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        left = 0
        right = len(height)-1
        while left<right:
                maxi = max(maxi, min(height[left],height[right])*(right-left))
                if height[left]<height[right]:
                    left += 1
                else:
                    right -= 1            
        return maxi 
