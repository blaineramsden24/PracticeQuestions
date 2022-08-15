class Solution(object):
    def groupAnagrams(self, strs):

        output = [[]]
        hold = set()

        for i in strs:
            countI = {}
            for c in range(len(strs)):
                countC = {}
                if c != i:






