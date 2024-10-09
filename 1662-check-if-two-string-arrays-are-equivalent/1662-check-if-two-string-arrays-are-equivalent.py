class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        return "".join(word1) == "".join(word2)
    
    # Time: O(n+m) where n is # chars in word1 and m is # chars in word2
    # Space: O(n+m)