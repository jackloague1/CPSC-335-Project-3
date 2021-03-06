array = [
   [2, 5, 9, 21],
   [-1, 0, 2], 
   [-10, 81, 121], 
   [4, 6, 12, 20, 150] 
]

Array_1 = [ 
    [2, 5, 9, 21],
    [-1, 0, 2],
    [-10, 81, 121],
    [4, 6, 12, 20, 150]
    ]

Array_2 = [ 
    [10, 17, 18, 21, 29],
    [-3, 0, 3, 7, 8, 11],
    [81, 88, 121, 131],
    [9, 11, 12, 19, 29]
    ]
Array_3  = [
    [-4, -2, 0, 2, 7],
    [4, 6, 12, 14],
    [10, 15, 25],
    [5, 6, 10, 20, 24]
    ]

finalArray = []         #array of all values in the array
sortedArray = []        #The sorted array of all values in the array
def merging(all_lists):
    #merges the values into one array
    for i in all_lists:
        for j in i:
            finalArray.append(j)
    #orders all the values in the array
    while finalArray:
        order = finalArray[0]
        for i in finalArray:
            if i < order:
                order = i
        sortedArray.append(order)
        finalArray.remove(order)

    print(sortedArray)
    sortedArray.clear()

#prints the sorted arrays
print("Sorted array for sample output:")
merging(array)
print("\n", "Sorted Array for Array_1: ")
merging(Array_1)
print("\n","Sorted Array for Array_2: ")
merging(Array_2)
print("\n","Sorted Array for Array_3: ")
merging(Array_3)
