
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdic = {}
        tdic = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sdic[s[i]] = 1 + sdic.get(s[i], 0 )
            tdic[t[i]] = 1 + tdic.get(t[i], 0)

        if sdic == tdic:
            return True
        else:
            return False

