class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        let_set = set()
        lt = 0 
        max_length = 0

        for rt in range(len(s)):
            while s[rt] in let_set:  
                let_set.remove(s[lt])
                lt += 1
            let_set.add(s[rt])
            max_length = max(max_length, rt - lt + 1)

        return max_length


