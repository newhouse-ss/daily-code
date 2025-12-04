class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}
        for i, val in enumerate(nums):
            if val in seen and i- seen[val] <= k:
                return True
            else:
                seen[val] = i

        return False
    
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        The idea is using a set to record the previous k nums of 
        the current val, when iterating the idx and num in nums,
        keep removing the num which with distance more than k to val
        then check if there are same num left in set, repeat nums exist
        with distance less than k, otherwise update val into set.

        """
        seen = set()
        for i, val in enumerate(nums):
            if i>k:
                seen.remove(i-k-1)
            if val in seen:
                return True
            
            seen.add(val)

        return False