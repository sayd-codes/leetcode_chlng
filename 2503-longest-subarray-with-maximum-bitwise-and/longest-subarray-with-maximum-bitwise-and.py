class Solution(object):
    def longestSubarray(self, nums):
        
        maxValue = float('-inf')
        maxRange = 0
        currentRange = 0

        for num in nums:
            if num > maxValue:
                maxValue = num
                maxRange = 1
                currentRange = 1
            elif num == maxValue:
                currentRange += 1
            else:
                currentRange = 0

            maxRange = max(maxRange, currentRange)

        return maxRange
        """
        :type nums: List[int]
        :rtype: int
        """
        