def sort_array(source_array):
    odd = []
    for i in source_array:
        if i %2 !=0:
            odd.append(i)
    odd.sort(reverse=True)
    for i in range(0,len(source_array)):
        if source_array[i] % 2:
            source_array[i] = odd[-1]
            odd.pop()
    return source_array



print(sort_array([5, 3, 2, 8, 1, 4]))

# outra forma de estrever

def sort_array(source_array):
    odd = sorted((i for i in source_array if i % 2), reverse= True)
    return [i if i % 2 == 0 else odd.pop() for i in source_array]



print(sort_array([5, 3, 2, 8, 1, 4]))
