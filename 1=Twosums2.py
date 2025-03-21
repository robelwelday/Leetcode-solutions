class Twosums:
       def __init__(self,nums,target):
           self.nums=nums
           self.target=target
       def result(self):
         num_dict = {}  
         for i, num in enumerate(self.nums):
             difference = self.target - num  
             if difference in num_dict:  
                 return (num_dict[difference], i)
             num_dict[num] = i 
         return None

        