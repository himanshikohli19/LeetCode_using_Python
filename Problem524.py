'''
524. Longest Word in Dictionary through Deleting

Given a string s and a string array dictionary,
return the longest string in the dictionary that can be formed
by deleting some of the given string characters.
If there is more than one possible result, return the longest word
with the smallest lexicographical order. If there is no possible result,
return the empty string.

Example 1:

Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
Example 2:

Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"
'''
#Complexity: O(mn)
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res=""
        maxLen=0
      
        
        for word in dictionary:
            pW=0
            pS=0
            while pW<len(word) and pS<len(s):
                if word[pW]==s[pS]:
                    pW+=1
                    pS+=1
                else:
                    pS+=1
            if pW==len(word): 
                if len(word)>maxLen or (len(word)==maxLen and word<res): 
                    res=word
                    maxLen=len(word)
                    
        return res
