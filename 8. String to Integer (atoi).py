class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:  
            return 0        
        sign = -1 if s[0] == "-" else 1  
        if s[0] in ["-", "+"]:
            s = s[1:]     
        j = len(s)
        count = 0
        x = 0
        for j in range(j - 1, -1, -1):
            if s[j].isdigit():
                x += int(s[j]) * (10 ** count)  
                count += 1
            else:
                x = 0
                count = 0
        x *= sign  
        min,max= -2**31, 2**31 - 1
        if x < min:
            return min
        if x > max:
            return max
        
        return x