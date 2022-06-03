import math
i = 2
count=0
num = 2
def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n)+1)):
        if (n%i==0):
            return False
    return True

while count < 10000:
    if(is_prime(i)):
        num = i
        count+=1
    i+=1

print(num)
