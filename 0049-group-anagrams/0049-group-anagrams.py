class Solution(object):
    def groupAnagrams(self, strs):
        
        res = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            
            for c in word:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(word)
        
        return res.values()
            