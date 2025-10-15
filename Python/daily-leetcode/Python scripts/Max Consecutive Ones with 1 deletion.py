class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = j = 0
        k = 1
        while j < len(nums):
            if nums[j] == 0:
                k -= 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
            j += 1
            current_max = j-i
        return current_max-1#因为是delete而不是上一题中的反转
    
solution = Solution()
print(solution.longestSubarray(nums = [1, 0, 1, 1]))