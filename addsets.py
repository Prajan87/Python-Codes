
def addset(set1,set2,set3):
    a = [i+j+k for i in set1 for j in set2 for k in set3 if i!=j|j!=k|k!=i]
    return a


if __name__=='__main__':
    set1 = set([12,3,65])
    set2 = set([1,23,3])
    set3 = set([23,0,45])
    data = addset(set1,set2,set3)
    print ('There are',len(data),'additions generated!')
    print (data)
