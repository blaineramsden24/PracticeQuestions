class Solution(object):
    def twoSum1(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

'''
Time Complexity --> O(n^2)

Space Complexity --> O(1)
'''

    def twoSum2(self, nums, target):
        hashMap = {}
        for i, num in enumerate(nums):
            if target - num in hashMap.keys():
                return [hashMap[target-num], i]
            hashMap[num] = i
        return


'''
Time Complexity --> O(n^2)

Space Complexity --> O(1)
'''
