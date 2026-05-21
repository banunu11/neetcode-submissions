class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        bob = 0
        for i in nums:
            if i not in check:
                check.add(i)
            else:
                bob = 1
                break
        if bob == 1:
            return True
        else: 
            return False