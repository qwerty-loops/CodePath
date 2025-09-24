def sum_of_digits(num):
    s=0
    while num >0:
        r=num%10
        num=num//10
        s=s+r
    return s



num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))