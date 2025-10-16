class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        新建一个height数组用来存放所有点的height，然后从头开始计算前序和
        在每次循环中将前序和的值赋值给height。
        """
        height = [0]
        presum = 0
        for i in range(len(gain)):
            presum += gain[i]
            height.append(presum)
        return max(height)