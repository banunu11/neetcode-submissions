class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 

        num = set(nums)
        print(num)
        length = 1
        maxl = 1

        for n in num:
            print(n)
            if n-1 not in num:
                while n + length in num:
                    length += 1
            else:
                length = 1
            maxl = max(length,maxl)
            print("s", length)
        return maxl
