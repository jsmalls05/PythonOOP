# 1. Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(someList):
    for i in range(0, len(someList), 1):
        if someList[i] >=1:
            someList[i] = "big"
    return someList

print(biggie_size([-1,3,5,-5]))

#2. Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(someList):
    total = 0
    for i in range(0, len(someList), 1):
        if someList[i] > 0:
            total += 1
    someList[len(someList)-1] = total
    return someList

print(count_positives([-1,1,1,1]))

#3. Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7

def sum(someList):
    total = 0
    for i in range(0,len(someList), 1):
        total += someList[i]
    return total

print(sum([1,2,3,4]))

#4. Average - Create a function that takes a list and returns the average of all the values.x
#Example: average([1,2,3,4]) should return 2.5

def average(someList):
    totalSum = sum(someList)
    avg = (totalSum)/len(someList)
    return avg

print(average([1,2,3,4]))

#5. Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0

def length(someList):
    return len(someList)

print(length([37,2,1,-9]))

#6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False

def minimum(someList):
    if len(someList) == 0:
        return False
    minVal = someList[0]
    for value in someList:
        if value < minVal:
            minVal = value

    return minVal

print(minimum([37,2,1,-9]))

#7. Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False

def maximum(someList):
    if len(someList) == 0:
        return False
    maxVal = someList[0]
    for value in someList:
        if value > maxVal:
            maxVal = value

    return maxVal

print(maximum([37,2,1,-9]))


#8. Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultAnalysis(someList):
    outPut = {}
    outPut['sumTotal'] = sum(someList)
    outPut['average'] = average(someList)
    outPut['minimum'] = minimum(someList)
    outPut['length'] = length(someList)
    return outPut

print(ultAnalysis([37,2,1,-9]))


#9. Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverseList(someList):
    for i in range(0, len(someList)//2, 1):
        temp =someList[i]
        someList[i] = someList[len(someList)-1-i]
        someList[len(someList)-1-i] = temp
    return someList

print(reverseList([37,2,1,-9]))