import math
def is_palindrome(n):
    rev_num = 0
    comp = n
    while n>0:
        rev_num = rev_num*10 + n%10
        n = math.floor(n/10)

    if rev_num == comp:
        return True
    else:
        return False

def largest_palindrome():
    n = 1
    for a in range (999, 99, -1):
        for b in range(a, 99, -1):
            if(is_palindrome(a*b)):
                if (a*b > n):
                    n=a*b
    return n

print(largest_palindrome())
