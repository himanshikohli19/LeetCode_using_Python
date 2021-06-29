#PROBLEM NUMBER: 680
#VALID PALINDROME II
'''
Given a string s, return true if the s can be palindrome
after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false
abcdefgedcba
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if(not s):
            return False
        
        start = 0
        end = len(s)-1
        
        while(start < end):
            if(s[start] != s[end]):
                if(s[start+1:end+1] == s[start+1:end+1][::-1]):
                    return True
                elif(s[start:end] == s[start:end][::-1]):
                    return True
                else:
                    return False
            start = start + 1
            end = end - 1
            
        return True


    


