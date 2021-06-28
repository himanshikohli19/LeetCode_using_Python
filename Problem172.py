#Problem 172:Factorial Trailing Zeroes
'''
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in
logarithmic time complexity?

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0

'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact=1
        count=0
        if n==0 and n%10!=0:
            return 0
        else:
            for i in range(1,n+1):
                fact=fact*i
            num=fact
            while num%10==0:
                count+=1
                num=num//10
            return count

#Another Solution
class Solution1:
    def trailingZeroes(self, n: int) -> int:
        count = 0                   
        i = 1                       
        while i <= 5:               
            count += (n//(5**i))    
            i += 1                       
        return count     

