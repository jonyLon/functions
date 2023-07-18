def power(num, s):
    if num == 0 and s <= 0:
        print("it is impossiable to raise 0 to a power less than 1")
    if num == 1 or num == 0:
        return num
    if s > 1:
        return num * power(num, s-1)
    if s < 1: 
        return 1/num * power(num, s+1)
    if s == 0:
        return 1
    return num

print(power(2,-8))


def forwardRange(a,b):
    if a <= b:
        print(a)
        forwardRange(a+1,b)
forwardRange(1,5)

def backwardRange(a,b):
    if a <= b:
        print(b)
        backwardRange(a,b-1)
backwardRange(1,5)

def palindrom(num):
    if num < 10:
        return num
    else:
        remainder = num % 10
        quotient = num // 10
    return int(str(remainder) + str(palindrom(quotient)))

print(palindrom(1245))


def sum(num):
    if num < 10:
        return num
    else:
        remainder = num % 10
        quotient = num // 10
    return remainder + sum(quotient)
print(sum(1235))


def parenthesis(a):
    if a > 0:
        print("(",end="")
        parenthesis(a-1)
        print(")",end="")

parenthesis(4)