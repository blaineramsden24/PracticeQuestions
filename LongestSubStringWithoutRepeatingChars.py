class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet = set()

        head = 0
        result = 0
        for tail in range(len(s)):
            while s[tail] in charSet:
                charSet.remove(s[head])
                head += 1
            charSet.add(s[tail])
            result = max(result, tail - head + 1)
        return result
