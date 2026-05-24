class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxw = 0

        if len(heights) == 2:
            return min(heights[r],heights[l])*(r-l)

        while r > l:
            area = min(heights[r],heights[l])*(r-l)
            if area > maxw:
                maxw = area
            if heights[r] > heights[l]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
            print(l, r, heights[r], heights[l], area, maxw)
    
        return maxw
                 
