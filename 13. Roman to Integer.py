class Solution:
    def romanToInt(self, s: str) -> int:
        coll=[("M",1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
        Num=0
        i=0
        while i < len(s):
            for string, value in coll:
                if s[i:i+len(string)] == string:  
                    Num += value
                    i += len(string)  
                    break 
        
        return Num