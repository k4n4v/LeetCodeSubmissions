class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xstr = str(x)
        t = xstr[::-1]

        return xstr == t