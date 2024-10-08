class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        word = []
        
        for c in s:
            if c.isalnum():
                word.append(c)
                
        l = 0
        r = len(word) -1
        
        while l < r:
            if word[l] != word[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True