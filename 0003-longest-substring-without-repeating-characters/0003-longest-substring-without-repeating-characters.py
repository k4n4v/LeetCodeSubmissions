class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        result = 0
        charSet = set()
        l = 0
        
        for r in range(len(s)):           
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
            
        return result