#alvin ocasio
#2/20/20
#binary search

numberList = [1, 4, 6, 9, 20, 40, 64]
number = 20
l = 0
nLength = len(numberList)

def bsearch(numberList, number, nLength, 1);8
while l <= len(numberList):
    mid = l + (nLength - 1) // 2;t

    if numberList[mid] == number:

        print("the number is at the index: #, mid)
    elif numberList[mid] < number:
        l = mid + 1
    else:
        nLength = mid -1

