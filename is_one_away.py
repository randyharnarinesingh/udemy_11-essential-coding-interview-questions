def is_one_away(A,B) :
    if len(A) == len(B) : # possible character change or equality case
        mismatch = False # tracks a single allowable mismatch between A and B
        for i in range(len(A)) :
            if not mismatch :
                if A[i] != B[i] :
                    mismatch = True
            else :
                if A[i] != B[i] :
                    return False
        return True
    elif len(A) == len(B) + 1 or len(A) == len(B) - 1 : # possible case of deletion/addition
        if len(A) > len(B) :
            longer = A
            shorter = B
        else :
            longer = B
            shorter = A
        mismatch = False
        for i in range(len(shorter)) :
            if not mismatch :
                if shorter[i] != longer[i] :
                    mismatch = True
            else :
                if shorter[i] != longer[i+1] :
                    return False
        if not mismatch :
            return True
        else :
            if shorter[i] == longer[i+1] :
                return True
            else :
                return False
    else :
        return False # string lengths indicate that one-away edits are not possible

print(is_one_away('abcde','abfde'))

print(is_one_away('abcde','abde'))
print(is_one_away('abcde','abcd'))
print(is_one_away('abcde','abce'))

print(is_one_away('xyz','xyaz'))
print(is_one_away('xyz','xyza'))
print(is_one_away('xyz','xyaa'))


