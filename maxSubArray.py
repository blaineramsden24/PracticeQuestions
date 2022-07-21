class Solution(object):
    def maxSubArray(self, nums):
        maxArray = []
        curSubArray = []
        for i in range (len(nums)):
            curSubArray.append(nums[i])
            curSubArray.append(nums)nums[i] + nums[i+1]
            if maxArray < curSubArray:
                maxArray =