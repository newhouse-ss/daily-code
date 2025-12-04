class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for element in nums1:
            if element in nums2:
                result.append(element)
                nums2.remove(element)
        return result