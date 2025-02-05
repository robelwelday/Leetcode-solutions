class twosum:
    def __init__(self,arrey,target):
        self.arrey=arrey
        self.target=target
    def result(self):
        for i in range(len(self.arrey)):
            for j in range(len(self.arrey)):
                if j!=i and self.arrey[j]+self.arrey[i]==self.target:
                    return (i,j)         
ass=twosum([1,2,8,6],9)
print(ass.result()) 
            
        


