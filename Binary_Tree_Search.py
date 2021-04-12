def BTS(sortedlist, temp_divi, r, input_value):
   
    mid_idx = temp_divi + (r - temp_divi) // 2  # floor division for example 5//2 = 2
    print("temp_divi ",temp_divi)
    print("middle index ", mid_idx)
    if r >= temp_divi:

        if sortedlist[mid_idx] == input_value:

            return mid_idx
        elif sortedlist[mid_idx] > input_value:


            return BTS(sortedlist, temp_divi, mid_idx - 1, input_value)
        else:
            return BTS(sortedlist, mid_idx + 1, r, input_value)

#when the input_-value > sorted_list[mid_indx] 
#arr = [ 1,2, 3, 4,5,6, 10, 40 ], input value = 10
#then in the second iteration we should calculate mid_idx like this

#mid_idx = temp_divi + (len_sorted_list - 1 - temp_divi) // 2
#but temp_divi = the index of mid_idx (from the 1st iteration) 
#for this example tem_divi in the second iteration = 2
              
            
    elif len_sorted_list == 0:
        print("this list is empty")
    else:
        return -1

arr = [ 1,2, 3, 4,5,6,7,8,9,10,20,21, 30, 40 ]
input_value = 10
result = BTS(arr, 0 , len(arr) -1, input_value)

if result != -1:
    print ("Element is present at index ", result)
else:
    print ("Element is not present in array")