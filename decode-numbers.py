class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        
        prev2 = 1 #dp[0]
        prev1 = 1 #dp[1]

        # recurrance
        for i in range(2, len(s)+1):
            curr = 0
            # single char: single digit; non-0
            if s[i-1] != '0':
                curr += prev1
            
            last_two = int(s[i-2:i])
            if last_two in range(10, 27):
                curr += prev2
            
            # iteration
            prev2 = prev1
            prev1 = curr
        
        return prev1
    

# use array to record results
class Solution(object):
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0]*(n+1)
        
        dp[0] = 1
        dp[1] = 1

        # recurrance
        for i in range(2, n+1):
            # single char: single digit; non-0
            if s[i-1] != '0':
                dp[i] += dp[i-1] # num of ways regarding i-th num as last position
            
            last_two = int(s[i-2:i])
            if last_two in range(10, 27):
                dp[i] += dp[i-2]
        
        return dp[n]
    
"""
Ultra-Short Explanation（你可以直接背）：

The key idea is dynamic programming.
Let dp[i] be the number of ways to decode the first i characters.

For each position, I check:

If the last one digit is valid (s[i-1] != '0'), I add dp[i-1].

If the last two digits form a valid number between 10 and 26, I add dp[i-2].

So dp[i] = valid_single * dp[i-1] + valid_double * dp[i-2].
With base cases dp[0] = 1, dp[1] = 1 if the first digit isn’t '0'.
"""