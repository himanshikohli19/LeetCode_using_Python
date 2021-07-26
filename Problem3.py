'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without
repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring,
"pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
'''

class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        str1 = ''
        max1 = 0
        for i in s:

            if i not in str1: 
                str1+=i
 
            else:
                str1 = str1[str1.index(i) + 1:] + i
            max1 = max(max1, len(str1))
        return max1
