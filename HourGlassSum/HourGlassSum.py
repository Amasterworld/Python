"""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in  is a subset of values with indices falling in this pattern in 's graphical representation:
a b c
  d
e f g

for example:

arr =

 -9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The  16 hourglass sums are:

    -63, -34, -9, 12,
-10,   0, 28, 23,
-27, -11, -2, 10,
  9,  17, 25, 18

the highest is 28


"""



def hourGlassSum(arr):

    list_value = []

    for i in range(len(arr)):
        for k in range(1,5):
            if i ==k:
                for j  in range (1, len(arr[0])-1):
                    #print(arr[i][j]," ", end ="")
                    print (arr[i-1][j-1], " ", arr[i-1][j], " ", arr[i-1][j+1]," ", arr[i+1][j-1]," ", arr[i+1][j]," ", arr[i+1][j+1] )
                    sum = arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
                    #print (sum)
                    list_value.append(sum)
    print(list_value)
    return max(list_value)








arr = [[1,1,1, 0,0,0],
       [0,1,0, 0,0,0],
       [1,1,1, 0,0,0],
       [0,0,2, 4,4,0],
       [0,0,0, 2,0,0],
       [0,0,1, 2,4,0]]

print(hourGlassSum(arr))
