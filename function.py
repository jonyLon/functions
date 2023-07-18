# def output():
#     print("\033[38;5;102m\'Don't let the noise of others\' opinions \ndrown out your own inner voice.")
#     print("\033[38;5;226mSteve Jobs")
#     print('\033[38;5;255m')

# output()

# def findOddNumsInRange(number1,number2):
#     while number1 <= number2:
#         if number1 % 2 != 0:
#             print(number1)
#         number1 += 1

# findOddNumsInRange(1,20)

# def drawTheLine(symbol, length, direction):
#     if direction == "h":
#         print(symbol*length)
#     elif direction == "v":
#         print((symbol+"\n")*length)
#     else:
#         print("Error")

# drawTheLine("*", 8, "v")
# drawTheLine("+", 8, "h")


# def maxNum(a, b, c, d):
#     list = [a, b, c, d]
#     print(max(list))

# maxNum(10,15,6,25)


# def sumOfTheRange(a,b):
#     print(sum(range(a,b)))

# sumOfTheRange(0,10)

# def isNumPrime(a):
#     simple = True
#     for i in range(2, a-1):
#         if a % i == 0:
#             simple = False
#         break
#     if simple:
#         return simple
#     else:
#         return simple
    
# print(isNumPrime(7),isNumPrime(10))

def isNumLucky(a):
    line = str(a)
    list = []
    list1 = []
    for n in line[0:3]:
        list.append(int(n))
    for n in line[3:6]:
        list1.append(int(n))
    if sum(list) == sum(list1):
        return True
    else:
        return False

print(isNumLucky(111111),isNumLucky(111565))