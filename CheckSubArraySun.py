class Solution(object):
    def checkSubarraySum(self, nums, k):

        for j in range(len(nums)):
            for i in range(len(nums)):
                if (sum(nums[j:i]) % k == 0) and len(nums[j:i]) >= 2:
                    return True

        return False
