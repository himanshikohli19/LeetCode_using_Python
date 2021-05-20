'''
Problem 231:

Given an integer n, return true if it is a power of two.
Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n>=0):
            if (n==0):
                return False        
            elif (n==1):
                return True 
            else:
                while(n>2):
                    if(n%2)!=0:
                        return False
                    n=n/2
            return True
        else:    
            return False   
