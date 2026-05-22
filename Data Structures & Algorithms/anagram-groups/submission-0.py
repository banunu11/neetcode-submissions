class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        dic = defaultdict(list)
        for s in strs:
            alp = [0]*26
            for x in s:
                alp[ord(x)-ord("a")] += 1
            dic[tuple(alp)].append(s)
        return list(dic.values())

