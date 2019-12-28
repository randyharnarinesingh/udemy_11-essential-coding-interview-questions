def most_frequent(array) :
    memory = {}
    max = 0

    for i in range(len(array)) :
        if array[i] in memory.keys() :
            memory[array[i]] += 1
        else :
            memory[array[i]] = 1

        if memory[array[i]] > max :
            max = memory[array[i]]
            maxkey = array[i]

    return maxkey

print(most_frequent([1,3,1,3,2,1]))