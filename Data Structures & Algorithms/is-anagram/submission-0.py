
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic, tdic = {}, {}
        if len(s) != len(t):
            return False

        for l in range(len(s)):
            sdic[s[l]] = sdic.get(s[l], 0) + 1
            tdic[t[l]] = tdic.get(t[l], 0) + 1

        return tdic == sdic

sol = Solution()
print(sol.isAnagram("racecar", "carrace"))



