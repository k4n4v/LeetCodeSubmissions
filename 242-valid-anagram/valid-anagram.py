class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = {}
        t_arr = {}

        for c in s:
            if c in s_arr:
                s_arr[c] += 1
            else:
                s_arr[c] = 1
        
        for c in t:
            if c in t_arr:
                t_arr[c] += 1
            else:
                t_arr[c] = 1

        return s_arr == t_arr

        # Time: O(n)
        # Space: O(n)
