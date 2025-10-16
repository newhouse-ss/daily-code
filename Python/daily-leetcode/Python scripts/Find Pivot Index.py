class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        if i+2 == j:
            if prefix == postfix:
                return i+1
        """
        presum, postsum = 0, sum(nums)
        for idx, ele in enumerate(nums):
            postsum -= ele
            if presum == postsum:#设计postsum和presum保证这次判断时，presum和postsum之间始终只隔一个数(可能的pivot)
                return idx
            presum += ele
        return -1

nums = [2, 1, -1]
solution = Solution()
print(solution.pivotIndex(nums))