numberList = [5,99,30,15,29,63,7]
nLength = len(numberList)

def bubbleSort(numberList, Nlength):
    for i in range(nLength):
        for j in range(0, nLength-i-1):

            if numberList[j] > numberList[j+1]:
                numberList[j], numberList[j+1] = numberList[j+1], numberList[j]

bubbleSort(numberList, Nlength):
print("bubble sort:", numberList)
bubbleSort(numberList, nLength)
print("bubble sort")

