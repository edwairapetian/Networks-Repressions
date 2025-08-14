def square(number):
    if number>64:
        raise ValueError("square must be between 1 and 64")
    if number<1:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    res=0
    for i in range(64):
        res+=2**(i)
    return  res
