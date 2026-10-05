class Solution:
    def maximumSubarraySum(self, nums, k):
        seen = set()
        curSum = 0
        maxSum = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] in seen or len(seen) == k:
                seen.remove(nums[left])
                curSum -= nums[left]
                left += 1

            curSum += nums[right]
            seen.add(nums[right])

            if len(seen) == k:
                maxSum = max(curSum, maxSum)

        return maxSum

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        