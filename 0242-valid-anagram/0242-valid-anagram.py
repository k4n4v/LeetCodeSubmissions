class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        dictS = dict()
        dictT = dict()
        
        for c in s:
            if c not in dictS:
                dictS[c] = 1
            else:
                dictS[c] += 1
        
        for y in t:
            if y not in dictT:
                dictT[y] = 1
            else:
                dictT[y] += 1
        
        return True if dictS == dictT else False
