import sys

def primes(d):
    for j in range (2,d):
        if (d%j)==0:
            return
    return d
    

def primefinder(data):
    for i in range (2,data):
        yield primes(i)
        
if __name__=='__main__' :
    primer = []
    for i in primefinder(int(sys.argv[1])):
        primer.append(i)
    print ([num for num in primer if isinstance(num,int)])
