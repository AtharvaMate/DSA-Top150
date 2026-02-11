class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        roman_num = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        
        i = 0
        while i < len(s):
            if i + 1 < len(s) and roman_num[s[i]] < roman_num[s[i+1]]:
                total += roman_num[s[i+1]] - roman_num[s[i]]
                i += 2
            else:
                total += roman_num[s[i]]
                i += 1
            
        return total