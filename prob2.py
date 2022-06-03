a = 0
first_no = 0
second_no = 1

while first_no < 4000000:
    if (second_no%2==0):
        a+=second_no
    else:
        a
    n = first_no
    first_no = second_no
    second_no = n + second_no
    print("Number is {}".format(second_no))

print(a)
