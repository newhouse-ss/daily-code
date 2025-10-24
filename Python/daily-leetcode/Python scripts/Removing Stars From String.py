class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        stack: array + pop()
        通过i遍历数组，遇到*的话就.pop(i)和.pop(i-1)
        """
        lst = []
        for i in s:
            if i == '*':
                lst.pop()
            else:
                lst.append(i)
        return ''.join(lst)
        
solution = Solution()
print(solution.removeStars(s = "leet**cod*e"))