class twosum:
    def __init__(self,arrey,target):
        self.arrey=arrey
        self.target=target
    def result(self):
        for i in range(len(self.arrey)):
            for j in range(len(self.arrey)):
                if j!=i and self.arrey[j]+self.arrey[i]==self.target:
                    return (i,j)         

            
        


