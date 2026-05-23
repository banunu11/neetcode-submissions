class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        pre = [1]*len(nums)
        post = [1]*len(nums)
        ans = []
        # print(pre, post)

        for x in range(1, len(nums)):
            pre[x] = nums[x-1] * pre[x-1]
            # print(pre, x, nums[j])

        for j in range(len(nums)-2, -1, -1):
            post[j] = nums[j+1] * post[j+1]
            # print(post, nums[j], j)

        for i in range(len(nums)):
            ans.append(pre[i] * post[i])

        return ans

