def common_elements(A, B) :
    common = []
    i = 0 # index for elements of A
    j = 0 # index for elements of B
    while i < len(A) and j < len(B) :
        if A[i] == B[j] :
            common.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j] :
            i += 1
        else :
            j += 1

    return common

print(common_elements([1,3,4,6,7,9],[1,2,4,5,9,10]))



