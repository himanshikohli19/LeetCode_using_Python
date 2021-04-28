##Given a roman numeral, convert it to an integer.
##
##Example 1:
##
##Input: s = "III"
##Output: 3
##Example 2:
##
##Input: s = "IV"
##Output: 4
##Example 3:
##
##Input: s = "IX"
##Output: 9
##Example 4:
##
##Input: s = "LVIII"
##Output: 58
##Explanation: L = 50, V= 5, III = 3.
##Example 5:
##
##Input: s = "MCMXCIV"
##Output: 1994
##Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        roman = {"M":1000, "CM":900, "D":500, "CD": 400,
                       "C":100,"XC":90, "L":50, "XL":40,
                       "X":10, "IX":9, "V":5, "IV":4, "I":1} #Dictionary created
        num = 0
        list1 = ["CM","CD","XC","XL","IX","IV"] #list for special romans
        for i in list1:
            if i in s:
                num = num + roman[i]
                s=s.replace(i,"") #replaced with blank to not get included in next iteration
        for i in s:
            num = num + roman[i]
        return(num)

        
        
