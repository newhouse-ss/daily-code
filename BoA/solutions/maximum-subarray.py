class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        key logic: If the current total has positive contribution to the later num, it should be kept.
        """
        maximum = total = nums[0]
        for i in range(1, len(nums)):
            if total + nums[i] > nums[i]:
                total += nums[i]
            else:
                total = nums[i]
            if total > maximum:
                maximum = total
        return maximum