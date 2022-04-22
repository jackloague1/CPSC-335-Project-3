def targetWords(Array_A, Array_B):
    Output_order = []
    Output_array = []
    j = 0

    # Iterate through each word in Array_B
    for k in range(0, len(Array_B)):
        j = 0
        # Iterate through each character in Array_A
        for i in range(0, len(Array_A[0])):
            # If character of Array_A ([0][i]) is equal to character ([j]) of word ([k]) in Array_B
            if Array_A[0][i] == Array_B[k][j]:
                # Move to next character of word in Array_B to check if it is also found in Array_A
                j = j + 1
            else:
                # If characters do not match, set j back to 0 to start at the begninning of word in Array_B
                j = 0
            # If j equals the length of the word in Array_B, the word must have been found in Array_A
            if (j == len(Array_B[k])):
                j = j - 1
                Output_order.append(i-j)
                Output_array.append(Array_A[0][i-j:i+1])
                break
    
    print(Output_order)
    print(Output_array)

Array_1A = ["sanoaklandrialtofullertonmarcolongchinocoronamodestoclovissimithousand"]
Array_1B = ["oakland", "modesto", "clovis", "corona"]
targetWords(Array_1A, Array_1B)