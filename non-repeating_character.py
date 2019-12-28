def non_repeating(string) :
    history = {}
    for i in range(len(string)) :
        if string[i] in history.keys() :
            history[string[i]] += 1
        else :
            history[string[i]] = 1
    result = ''
    for key in history.keys() :
        if history[key] == 1 :
            return key
    return None

print(non_repeating('aabcb'))
print(non_repeating('xxyz'))
print(non_repeating('aabb'))
print(non_repeating('aabbbc'))