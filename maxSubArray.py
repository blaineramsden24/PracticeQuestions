class Solution(object):
    def maxSubArray(self, nums):
        maxArray = nums[0]
        curSubArray = 0
        for n in nums:
            if curSubArray < 0:
                curSubArray = 0
            curSubArray += n
            maxArray = max(curSubArray, maxArray)
        return maxArray
