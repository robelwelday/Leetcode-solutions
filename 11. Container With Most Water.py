class Solution:
    def maxArea(self, height: List[int]) -> int:
        lt, rt = 0, len(height) - 1
        maxi= 0
        
        while lt < rt:
            area = min(height[lt], height[rt]) * (rt - lt)
            maxi= max(maxi, area)
        
            if height[lt] < height[rt]:
                lt += 1
            else:
                rt -= 1
        
        return maxi



        