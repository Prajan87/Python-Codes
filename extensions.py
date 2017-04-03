def changer(ext):
    net = []
    edu = []
    com = []
    new_ext = {}
    for i in ext:
        lent = len(ext[i])
        if(ext[i][lent-3:lent] == 'net'):
            net.append(i)
        if(ext[i][lent-3:lent] == 'edu'):
            edu.append(i)
        if(ext[i][lent-3:lent] == 'com'):
            com.append(i)
    new_ext = {'net':set(net),'edu':set(edu),'com':set(com)}
    return new_ext
    
if __name__=='__main__':
    ext = {'UTSA':'www.utsa.edu', 'AMD':'www.amd.com','Intel':'www.intel.com','fake':'iamfake.net','google':'www.google.com','UTAustin':'www.utexas.edu'}
    new_ext = changer(ext)
    print ('net :', new_ext['net'])
    print ('edu :', new_ext['edu'])
    print ('com :', new_ext['com'])
