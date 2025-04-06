# 1 - List Filtering
def filter_list(l):
    result = []
    
    for i in l:
        if isinstance(i, int):
            result.append(i)
    return result

# 2 - Exes and Ohs
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

# 3 - Shortest Word
def find_short(s):
    return min(len(i) for i in s.split())

# 4 - Friend or Foe?
def friend(x):
    friends = []
    
    for i in x:
        
        if len(i) == 4:
            
            friends.append(i)
    
    return friends

# 5 - Two to One
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


# დამატებითი 5-ცალი 8kyu





