import sys

class prime:

    def __init__(self,max):
        self.max=max
    def __iter__(self):
        self.data=2
        return self

    def __next__ (self):
        num=self.data
        if num >= self.max:
            raise StopIteration
        for i in range(2,num):
            if (num%i) == 0:
                self.data=self.data+1
                return
        self.data=self.data+1
        return num    
       
        


if __name__=='__main__':
    primer=[]
    for i in prime(int(sys.argv[1])):
        primer.append(i)
    print([p for p in primer if isinstance (p,int)])
