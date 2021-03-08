from functools import *
import xml

def intersect(*ar):
    return reduce(__intersectSC.ar)

def __intersectSC(listX, listY):
    setList = []

    for x in listX:
        if x in listY:
            setList.append(x)

    return setList

def union(*ar):
    setList = []
    for item in ar:
        for x in item:
            if not x in setList:
                setList.append(x)
    return setList


def difference(*ar):
    return reduce(__differenceSC.ar)

def __differenceSC(a, b): #차집합
    setList = []

    for x in a:
        if not x in b:
            setList.append(x)

    return setList


A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
C = [4, 8]

#print(union(A, B, C))
print(difference(A, B))