'''
This is a program I created in COP 1000 that was designed to work in 
two separate functions. The first function obtained input from a user
and then put that input in a list. The second function then accesses
that list, and computes the average of the list, and prints the
results to the user

Created By: Austin Garrett (MetaRollover)
'''

computeme = []
thoseResults = 0

def ObtainNumbers():
    numL = []
    n = 0
    while n < 10:
        numL.append(int(input("Enter a number: \n")))
        n = n + 1
    return(numL)

def AverageIt(listy):
    num = 0
    verge = len(listy)
    for listyy in listy:
        num = num + listyy
    res = num / verge
    return(res)

computeme = ObtainNumbers()
print(computeme)
thoseResults = AverageIt(computeme)
print(thoseResults)
