'''
PROBLEM 290: Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic={}
        lst1= list(pattern)
        lst2= list(s.split())
        
        if len(lst1)!=len(lst2):
            return False
        
        for k,v in zip(lst1,lst2):
            if k not in dic and v not in dic.values(): 
                dic[k]=v
            else:
                if k not in dic.keys() or dic[k]!=v :
                    return False
        return True
        
