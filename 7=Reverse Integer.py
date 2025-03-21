class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            st = "-" + str(x)[:0:-1] 
        else:
            st = str(x)[::-1]
        x=int(st) 
        return self.check_range(x) 
    def check_range(self,x):
      return x if -2**31 < x < 2**31 else 0
                
        
         
        