def sumOfTheList(a = [1,2,3]):
    print(sum(a))

sumOfTheList()

def maxOfTheList(a = [1,2,3]):
    print(max(a))

maxOfTheList()

def listAnalysis(a = [1,2,3,-5,-6,-3]):
    countPositive = 0
    countNegative = 0
    countCouples = 0
    countOdd = 0
    for n in a:
        if n > 0:
            countPositive += 1
        elif n < 0: 
            countNegative += 1
        if n % 2 != 0:
            countOdd += 1
        elif n % 2 == 0:
            countCouples += 1
    print("Positive\tNegative\tCouples\t\tOdd")
    print("{}\t\t{}\t\t{}\t\t{}".format(countPositive, countNegative, countCouples, countOdd))
listAnalysis()


def listContents(a = [1,2,3,-5,-6,-3]):
    for i in a:
      print(i,"\t",end="")
    print()
listContents()

def findNumInTheList(num, a = [1,2,3,-5,-6,-3]):
    if a.count(num) == 0:
        print("Number {} does not exist in this list".format(num))
    else:
        print("Number {} exists in this list".format(num))

findNumInTheList(5)
findNumInTheList(-5)


def findFactorialForElemInList(a = [1,2,3,5,6,7]):
    list = []
    for i in a:
        factorial = 1
        while i > 0:
            factorial *= i
            i -= 1
        list.append(factorial)
    print(list)

findFactorialForElemInList()

