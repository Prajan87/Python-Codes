import re
import sys

class roman:

    def __init__(self,num):
        self.num=num

    def pattern_checker(self):
        pattern = '^(X[LC]|L?X{0,3})(I[VX]|V?I{0,3})$'
        if (re.search(pattern,self.num)):
            return True
        else:
            return False


if __name__=='__main__':
    rom = roman(sys.argv[1])
    if  (rom.pattern_checker()):
        print (sys.argv[1], 'is valid')
    else:
        print (sys.argv[1], 'is not valid')
