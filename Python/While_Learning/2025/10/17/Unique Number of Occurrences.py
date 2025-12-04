class Solution:
    def uniqueOccurrences(self, arr):
        """
        argu: array of numbers
        return: boolean
        借鉴计数排序
        """
        length = len(arr)
        count = {}#To count the occurence number of values, 因为数组从零开始，所以这里要+1.
        for i in range(length):
            key = arr[i]
            if str(key) not in count.keys():
                count[str(key)] = 1
            else:
                count[str(key)] += 1
        count_values = count.values()
        set_count_values = set(count_values)
        if len(count_values) == len(set_count_values):
            return True
        return False

arr = [16,16,10,12,10,13,-1,-1,10,12,12,-1,12,10,10]
solurion = Solution()
print(solurion.uniqueOccurrences(arr))