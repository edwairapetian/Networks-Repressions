def is_armstrong_number(number):
    sum=0
    num=number
    count=len(str(num))
    res=False
    for i in range(count):
        k = num%(10**(i+1))
        num=num-k
        k//=10**i
        sum += k**count
    if sum==number:
        res=True
    return res

