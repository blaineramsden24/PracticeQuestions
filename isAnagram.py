class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        countS, countT = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(countS)):
            countS[i] = 1 + countS.get(s[i], 0)
            countT[i] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
