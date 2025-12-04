class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_idx = {}
        for i in range(len(nums)):
            num_idx[nums[i]] = i#桶排序
        for i in range(len(nums)):
            component = target-nums[i]
            if component in num_idx and num_idx[component] != i:
                return i, num_idx[component]