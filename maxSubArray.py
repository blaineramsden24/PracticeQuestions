class Solution(object):
    def maxSubArray(self, nums):
        maxArray = nums[0]
        curSubArray = nums[0]
        for n in nums:

            if sum(curSubArray) > sum(maxArray):
                maxArray = curSubArray
