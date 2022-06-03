import math
list = []
multiple = 1
def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n)+1)):
        if (n%i==0):
            return False
    return True

for i in range(2,21):
    if(is_prime(i)):
        multiple*=i
        list.append(i)
    else:
        num = i
        for j in list:
            if (num%j == 0):
                num = num/j

        if(is_prime(num)):
            multiple*=num
            print("{} is {}".format(i, num))
            list.append(num)
        else:
            k=2
            while (k<num):
                if(num%k == 0):
                    num = num/k
                    list.append(k)
                    k+=1
            multiple *= num

print(multiple)
