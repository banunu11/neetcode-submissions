class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        print(nums)

        for a, x in enumerate(nums):
            if a > 0 and x == nums[a-1]:
                continue
            
            l, r = a+1, len(nums)-1
            while l < r:
                target = 0-x
                if nums[r] + nums[l] == target:
                    ans.append([x, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif nums[r] + nums[l] < target:
                    l += 1
                else:
                    r -= 1
        
        return ans
            

