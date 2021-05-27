'''
Problem 258:
Given an integer num, repeatedly
add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0
'''


class Solution:
    def addDigits(self, num: int) -> int:
        sum1=0
        while num>0:
            sum1 += num%10
            num=num//10
            if num == 0 and sum1>9:
                num=sum1
                sum1=0
        return sum1

#Another Solution
class Solution1:
    def addDigits(self, num: int) -> int:
        while num // 10 > 0:
            num = sum([int(i) for i in str(num)])
        return num
