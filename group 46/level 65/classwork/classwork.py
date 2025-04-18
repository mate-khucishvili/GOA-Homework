# 1 -


# 2 - 


# 3 -


# 4 - Breaking chocolate problem
def breakChocolate(n, m):
    if n > 0 and m > 0:
        return m*n - 1
    else:
        return 0
    
# 5 - Anagram Detection
def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower())

# 6 - Are the numbers in order?
def in_asc_order(arr):
    return arr == sorted(arr)

# 7 - Flatten and sort an array
def flatten_and_sort(array):
    new_list= []
    for i in array:
        new_list += i 
    return sorted(new_list)