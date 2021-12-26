"""
Problem Link: https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string, find the first non-repeating character in it and return 
it's index. If it doesn't exist, return -1.
Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
# Time Complexity: O(n*n)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeat_ele=[]
        for i in range(len(s)):
            if (s[i] in s[i+1:]) and (s[i] not in repeat_ele):
                ele=s[i]
                repeat_ele.append(ele)
            elif (s[i] in repeat_ele):
                index=-1
            else:
                index=i
                break

        return index
            
            
      
