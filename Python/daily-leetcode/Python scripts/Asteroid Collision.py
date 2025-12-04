class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        思路是从头到尾遍历，使用head, end记录一段连续正数，如果遇到一个负数的话，从尾到头遍历
        [head, end]数组，直到遇到比当前负数abs大或者是[head, end]数组为空了，则结束当次对该负数
        的交互，检查下一个数。
        """
        survive_lst = []
        for ast in asteroids:
            while survive_lst and ast < 0 < survive_lst[-1]:
                if abs(ast) > survive_lst[-1]:
                    survive_lst.pop()
                    continue
                elif abs(ast) ==  survive_lst[-1]:
                    survive_lst.pop()
                break#ast小于等于前面遇到的positive行星
            else:#如果while是正常结束的，ast大于前面遇到的所有positive行星
                survive_lst.append(ast)
        return survive_lst
                
solution = Solution()
print(solution.asteroidCollision(asteroids=[2, -2, -2]))