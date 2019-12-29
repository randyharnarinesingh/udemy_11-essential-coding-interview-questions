def is_rotation(A,B) :
    n = len(A)
    key = A[0]
    for j in range(n) :
        if B[j] == key :
            break

    if B[j] == key : # something was matched, check for a further (n-1) matches
        for i in range(1,n) :
            j = (j+1) % n # ensures index doesn't overflow and instead loops from end to beginning
            if A[i] != B[j] :
                return False
        return True

    else :
        return False



print(is_rotation([1,2,3,4,5,6,7],[4,5,6,7,1,2,3]))