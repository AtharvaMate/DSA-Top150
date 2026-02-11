class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        chars = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        l = []

        for i in range(len(values)):
            count = int(num / values[i])
            num = num % values[i]
            l.append(count)
        
        return "".join(chars[j]*l[j] for j in range(len(l)))
            