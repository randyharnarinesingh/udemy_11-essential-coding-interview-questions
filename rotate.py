def view_arrays(field) :
    for row in field:
        print('   '.join(list(map(str, row))))

def rotate(given_array,n) :
    new_array = [ [0 for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            new_array[j][n-i-1] = given_array[i][j]
    return new_array

array = [[1,2,3],[4,5,6],[7,8,9]]
view_arrays(array)
print()
view_arrays(rotate(array,3))
