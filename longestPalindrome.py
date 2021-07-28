import os
import re
import sys

class Solution:

    def longestPalindrome(self, s: str) -> str:
        size = len(s)

        if size <= 1:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]
        print(dp)
        longest_l = 1

        res = s[0]

        # dp[i+1][j-1]
        # j-1-(i+1)+1 = j-i-1
        # j-i-1 < 2 ; only 1
        # j-i <3; ( j-i+1 < 4 )

        for j in range(1, size):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j-i+1 > longest_l:
                    longest_l = j-i+1
                    res = s[i:j+1]



                #if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                #    dp[l][r] = True
                #    cur_len = r - l + 1
                #    if cur_len > longest_l:
                #        longest_l = cur_len
                #        res = s[l:r + 1]


        return res

