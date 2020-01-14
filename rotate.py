def view_arrays(field) :
    for row in field:
        print('  '.join(list(map(str, row))))

def rotate(given_array,n) :
    new_array = [ [0 for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            new_array[j][n-i-1] = given_array[i][j]
    return new_array

def increment_position(posi,posj,increments,a,b,c,d) : # helper function used to assist in single swaps of array elements
    count = 0
    while count < increments :
        if posi == a and posj < d :
            posj += 1
        elif posj == d and posi < b :
            posi += 1
        elif posi == b and posj > c :
            posj -= 1
        elif posj == c and posi > a :
            posi -= 1
        count += 1
    return posi, posj

def rotate_sub_array(given_array,starti,startj,n) :
    for i in range(n-1) :
        posi = starti
        posj = startj + i
        stored = given_array[posi][posj]
        count = 0
        while count < 4 :
            posi,posj = increment_position(posi,posj,n-1,starti,starti+n-1,startj,startj+n-1)
            stored,given_array[posi][posj] = given_array[posi][posj],stored
            count += 1

    return given_array

def rotate_in_place(given_array,n) :
    top = 0
    left = 0
    while n > 1 :
        given_array = rotate_sub_array(given_array,top,left,n)
        top = top + 1
        left = left + 1
        n -= 2

    return given_array

array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
view_arrays(array)
print()
view_arrays(rotate_in_place(array,4))

