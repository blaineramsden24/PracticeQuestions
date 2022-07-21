class Solution(object):
    def search(self, nums, target):

        high = len(nums)
        low = 0
        mid = (high + low) // 2
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid
            elif nums[mid] > target:
                high = mid
            else:
                return mid
        return -1