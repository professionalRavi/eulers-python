a = 0
for i in range(1000):
    if(i%3 == 0 or i%5 == 0):
        print("Number is {}".format(i))
        a +=i
        print("Sum is {}".format(a))
    else:
        a
print(a)
