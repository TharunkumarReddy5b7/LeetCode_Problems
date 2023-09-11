#P13_RomanToInteger
class Solution:
    def romanToInt(self, s: str) -> int:
        num_map = {

             "I":1,
             "V":5,     "IV":4,
             "X":10,   "IX":9,
             "L":50,    "XL":40,
             "C":100,  "XC":90,
             "D":500,   "CD":400,
             "M":1000, "CM":900,
        }

        a=0

        q=""

        for i in s:
            
            if q+i in num_map:
                q=q+i
                continue
            else:
                
                d=num_map[q]
                a+=d
                q=i
        return a+num_map[q]
        
        