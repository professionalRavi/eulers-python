import math
que = 600851475143
def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n)+1)):
        if (n%i==0):
            return False
    return True

def findnum():
    if (is_prime(que)):
            return que
    else:
        start = math.ceil(math.sqrt(que)+1)
        while start>=2:
            if(is_prime(start)):
                if (que%start==0):
                    print(start)
                    return
                else:
                    start-=1
            else:
                start-=1

findnum()
