

# Driver Code
arr = [2, 3, 4, 10,22,24,26,27, 39, 41,50,55,67,78,90,100,101.102,103,104 ]

closest_value = []
def BS (sortedList, input_value):

    initial_divi  = 0
    TheMaxInd_sortedList = len (sortedList) - 1 # minus 1 to be suitable with the index
    arr = sortedList
   # last_mid = 0
    while initial_divi <= TheMaxInd_sortedList:
        mid = initial_divi + (TheMaxInd_sortedList - initial_divi) // 2
        print ("mid = ", mid)

        if arr[mid] == input_value: # (1)
            return mid
        elif arr[mid] < input_value:
            initial_divi = mid + 1
            last_mid = mid
            print("value at current mid",mid," ", arr[mid])
            print("initial divi =", initial_divi)
            closest_value.append(arr[last_mid])
        elif arr[mid] > input_value:
            TheMaxInd_sortedList = mid - 1 #  mid - 1 because arr[mid] had compared at (1)
            print("initial divi =", initial_divi)
            print("value at current mid", mid, " ", arr[mid])
            last_mid = mid
            print("last mid =", last_mid)
            closest_value.append(arr[last_mid])

    print ("last mid",last_mid)
    #raise Exception ("n is not in the list")


print ("the given list is ", arr)
print (" The index of the input value is ",BS(arr,38))
print ("the list of closes value ", closest_value)