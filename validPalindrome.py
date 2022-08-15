class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for c in s:
            if c.isalnum():
                newstr =+ c
        return newstr == newstr[::-1]

