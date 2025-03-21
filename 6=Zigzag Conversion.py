class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s)<=numRows:
            return s
        id,st=0,1;
        rows=[""]*numRows
        for st in s:
        
         rows[id] += st
         if id == 0:
            step = 1  
         elif id == numRows - 1:
            step = -1  
         id+= step
        return "".join(rows)

