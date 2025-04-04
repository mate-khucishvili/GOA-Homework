# 1 - Get the mean of an array
def get_average(marks):
    return int(sum(marks) / len(marks))

# 2 - Total amount of points
def points(games):
    result = 0
    for i in games:
        
        x = int(i[0])
        y = int(i[2])
        
        if x>y:
            result += 3
        elif x==y:
            result += 1
    
    return result

# 3 - 

# 4 - 

# 5 - 

# 6 - 

# 7 - 

# 8 - 
