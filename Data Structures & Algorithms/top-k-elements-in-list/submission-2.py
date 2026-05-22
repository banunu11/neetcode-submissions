class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, s in count.items():
            freq[s].append(n)
            
        ans = []
        for i in range(len(freq)-1, 0, -1):
            for x in freq[i]:
                ans.append(x)
                if len(ans) == k:
                    return ans