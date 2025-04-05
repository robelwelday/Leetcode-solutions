class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        prefix=strs[0]
        i=0
        for s in strs[1:]:
            j=0
            while j < min(len(prefix), len(s)) and prefix[j] == s[j]:
                j+=1
            prefix = "" if j == 0 else prefix[:j]
        return prefix