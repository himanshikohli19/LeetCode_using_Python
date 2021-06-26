#PROBLEM 125
#VALID PALINDROME
'''
Given a string s, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
 
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str2,str3,str4="","",""
        for i in s:
            if i.isalnum():
                str2+=i
        str3=str2.lower()
        str4=str3[::-1]
        if str4==str3:
            return True
        else:
            return False
        

