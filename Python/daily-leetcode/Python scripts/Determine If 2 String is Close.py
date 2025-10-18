class Solution:
    def closeStrings(self, word1, word2):
        """
        argus: word1, word2, strings
        return: boolean 
        猜测：只要字符串中出现的各个元素个数是互异的就可以换，按照上一个问题的思路计数一下再求set。
        bba, acc就不行，所以还需满足两个set相减=0，也就是说所有元素相同。
        计数数组中的个数也必须是对应相同的（比如说：14523和23541必须对应相同）
        综上，首先长度得相同，其次计数字典的key组成的set相减需要是0，并且value组成的set相减也必须是0
        aaaabc-->caaaba, cabbba
        """
        count1 = {}
        count2 = {}
        length = len(word1)
        if len(word2) != length:
            return False
        for i in range(length):
            if word1[i] not in count1:
                count1[word1[i]] = 1
            else:
                count1[word1[i]] += 1
            if word2[i] not in count2:
                count2[word2[i]] = 1
            else:
                count2[word2[i]] += 1
        set1_keys = set(count1.keys())
        set2_keys = set(count2.keys())
        if set1_keys-set2_keys != set():
            return False
        
        values1_sorted = sorted(count1.values())
        values2_sorted = sorted(count2.values())
        for i in range(len(values1_sorted)):
            if values1_sorted[i] != values2_sorted[i]:
                return False
        return True

word1 = "aaabbbbccddeeeeefffff"
word2 = "aaaaabbcccdddeeeeffff"
solution = Solution()
print(solution.closeStrings(word1, word2))