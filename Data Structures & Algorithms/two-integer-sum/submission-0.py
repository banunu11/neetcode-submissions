import numpy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        
        dic = {}
        for i, x in enumerate(nums):
            diff = target - x 
            if diff in dic:
                return [dic[diff], i] 
            dic[x] = i






