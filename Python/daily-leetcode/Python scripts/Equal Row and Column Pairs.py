class Solution:
    def equalPairs(self, grid):
        """
        思路是，先通过简单的sum把每一行的和求出来，然后通过遍历的方式计算列的和。
        题意理解错误，要求找的是完全相同的行列而不是和相等的行列。
        """
        m = {}
        total = 0
        for row in grid:
            if str(row) not in m.keys():
                m[str(row)] = 1
                continue
            m[str(row)] += 1
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            if str(col) in m.keys():
                total += m[str(col)]
        return total

solution = Solution()
print(solution.equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))