class Solution(object):
    total = 0
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        can not rob adjacent house on same night.
        [1, 1000, 2, 3]
        idea: sort nums[] first, visit the sorted array in a reverse order, create a empty array E, 
        append its idx, then keep checking whether the left&right neighbors in array E, if not, append.The method is wrong, since after sorting, the relative relationship will be changed.
        
        max+recurrance
        """
        if not nums:
            return 

        current = nums[0]
        index = 0
        for i in range(len(nums)):
            if nums[i] > current:
                current = nums[i]
                index = i
        self.total += current
        self.rob(nums[0:index])
        self.rob(nums[index+2:len(nums)])
        return self.total
        
    
solution = Solution()
print(solution.rob([1,2,3,1]))