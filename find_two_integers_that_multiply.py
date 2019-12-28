def func(array,num) :
    required = []
    if num % array[0] == 0 : # num might be not 
        required.append(int(num/array[0]))
    for k in range(1,len(array)) :
        if array[k] in required :
            return True
        else :
            if num % array[k] == 0 :
                required.append(int(num/array[k]))
    return False

print(func([2,4,1,6,5,40,-1],20))