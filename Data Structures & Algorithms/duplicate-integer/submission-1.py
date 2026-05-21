class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        bob = 0
        for i in nums:
            if i not in check:
                check.add(i)
            else:
                return True
        
        return False