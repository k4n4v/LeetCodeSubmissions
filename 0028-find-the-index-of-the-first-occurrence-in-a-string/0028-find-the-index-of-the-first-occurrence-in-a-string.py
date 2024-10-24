class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0

        # We only need to loop till len_h - len_n + 1 because there's no point in checking the last few characters where the needle can't fit
        for i in range(len(haystack) - len(needle) + 1):
            # Two pointers to compare the haystack and the needle
            j = 0
            while j < len(needle) and haystack[i + j] == needle[j]:
                j += 1
            # If we matched the whole needle, return the starting index
            if j == len(needle):
                return i

        # If no match is found, return -1
        return -1