import sys
prime = []
def find_prime(data):
    for i in range (2, data):
        if (data%i) == 0:
            return False
    return True

for i in range(2,int(sys.argv[1])):
    if find_prime(i):
        prime.append(i)
print(prime)
