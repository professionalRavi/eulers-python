import math
i=2
sum = 0
def is_prime(n):
    if (n==2):
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(n)+1)):
            if (n%i==0):
                return False
        return True

while i<2_000_000:

    if(is_prime(i)):
        sum+=i
    i+=1

print(sum)
