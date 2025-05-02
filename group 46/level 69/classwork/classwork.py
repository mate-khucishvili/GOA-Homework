# 1- Printer Errors
def printer_error(s):
    kargi_nawili = "abcdefghijklm"
    
    erorebis_raodenoba = 0
    for i in s:
        if i not in kargi_nawili:
            erorebis_raodenoba += 1

    sabolo_sigrzde = len(s)

    return f"{erorebis_raodenoba}/{sabolo_sigrzde}"
# 2- Don't give me five!
def dont_give_me_five(start, end):
    count = 0  
    for i in range(start, end + 1): 
        if '5' not in str(i):
            count += 1
    return count
# 3- Triangular Treasure
def triangular(n):
    if n <= 0:
        return 0
    return n * (n + 1) // 2

# 4- Sorted? yes? no? how?
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr)[::-1]: 
        return "yes, descending"
    else:
        return "no"
# 5-Bumps in the Road
def bumps(road):
    if road.count('n') <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"