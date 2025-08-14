def steps(number):
    num=0
    if number<1:
        raise ValueError("Only positive integers are allowed")
    while number!=1:
        if number%2:
            number=number*3+1
        else:
            number/=2
        num+=1
    return num
