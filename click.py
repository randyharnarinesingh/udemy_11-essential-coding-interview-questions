def view_field(field) :
    for row in field:
        print('   '.join(list(map(str, row))))

def click(field,num_rows,num_cols,given_i,given_j) : # can speed up using dynamic programming to track visited spots using flags
    if field[given_i][given_j] != 0 :
        return field
    else :
        field[given_i][given_j] = -2
        for i in [given_i-1,given_i,given_i+1] :
            for j in [given_j-1,given_j,given_j+1] :
                if 0 <= i < num_rows and 0 <= j < num_cols :
                    field = click(field,num_rows,num_cols,i,j)
        return field

'''field = [[0,0,0,0,0],[0,1,1,1,0],[0,1,-1,1,0]]
num_rows = 3
num_cols = 5
given_i = 0
given_j = 1'''

field = [[-1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,-1]]
num_rows = 4
num_cols = 4
given_i = 1
given_j = 3

view_field(field)
field = click(field,num_rows,num_cols,given_i,given_j)
print()
view_field(field)