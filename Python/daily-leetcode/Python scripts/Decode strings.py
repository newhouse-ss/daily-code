class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        遍历整个字符串，当遇到数字时(index == i)，令i+2为start，下一个]的前一位为end，重复的append(中间的元素)
        """
        self.i = 0
        return self.decode(s)
    def decode(self, s):
        result, num = '', 0
        while self.i < len(s):
            c =  s[self.i]
            if c.isdigit():
                num = num*10 + int(c)
                self.i += 1
            elif c == '[':
                self.i += 1
                inner = self.decode(s)
                result += inner*num
                num = 0
            elif c == ']':
                self.i += 1
                return result
            else:
                result += c
                self.i += 1
        return result