#Problem 204
#Count the number of prime numbers less than a non-negative number, n.

class Solution:
    def countPrimes(self, n: int) -> int:
        #print first N prime numbers
        c=0
        i=2
        while (i<n):
            for j in range(2,i):
                if (i%j==0):
                    i+=1
                    break

            else:
                c+=1
                i+=1
        
        return c
