class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        left = 0
        right = len(s_clean) - 1 

        while left < right:
            if s_clean[left] != s_clean[right]:
                return False
            left += 1
            right -= 1

        return True