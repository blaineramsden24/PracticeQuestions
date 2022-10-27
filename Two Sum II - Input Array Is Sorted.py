class Solution(object):
    def twoSum(self, numbers, target):
        lPointer = 0
        rPointer = len(numbers) - 1

        while lPointer < rPointer:
            total = numbers[lPointer] + numbers[rPointer]
            if total == target:
                return [lPointer + 1, rPointer + 1]
            elif total > target:
                rPointer = rPointer - 1
            else:
                lPointer = lPointer + 1

