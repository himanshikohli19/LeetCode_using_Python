#344. Reverse String
#Write a function that reverses a string.
#The input string is given as an array of characters s.

#Example 1:
#Input: s = ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]


class Solution:
    def reverseString(self, s):
        n=len(s)
        for i in range(n):
            if i < (n-1):
                s[i],s[n-1]=s[n-1],s[i]
                n-=1
            else:
                continue

        print(s)
    
    
