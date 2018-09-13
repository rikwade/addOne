#!/usr/bin/env python3

'''
[1,3,4]->[1,3,5]
[1,9,9]->[2,0,0]
[9,9,9]->[1,0,0,0]
'''
def addOne(inArray):
    # create a copy of the inArray
    tmpArray = inArray.copy()
    carry = 1

    for i in range(len(tmpArray),0,-1):
        pos = i-1
        tmpArray[pos] = tmpArray[pos]+carry
        if (tmpArray[pos] > 9):
            tmpArray[pos] = 0
            carry = 1
        else:
            carry = 0

    if (carry == 1):
        tmpArray.insert(0,1)

    return(tmpArray)

#Main
newArray = addOne([9,2])

print("newArray:", newArray)
