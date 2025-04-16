# 1 - Isograms
def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))
 
# 2 - Jaden Casing Strings
def to_jaden_case(string):
    # გაყოფა სიტყვებად
    words = string.split()
    

    capitalized_words = [word.capitalize() for word in words]
    
    # დაბრუნდება გაერთიანებული სია
    return ' '.join(capitalized_words)

# 3 - Mumbling
def accum(st):
    # ცარიელი სია თითოეული გარდაქმნილი ნაწილისთვის
    parts = []
    
    for i, char in enumerate(st):
        # დიდი ასო + იგივე პატარა ასოები i-ჯერ
        part = char.upper() + char.lower() * i
        
        # დამუშავებული ნაწილის დამატება სიაში
        parts.append(part)
    
    # ყველა ნაწილის შეერთება ტირეებით
    return '-'.join(parts)
 
# 4 - Regex validate PIN code
def validate_pin(pin):
    
    if len(pin) == 4 or len(pin) == 6:
        
        if pin.isdigit():
            return True  
        else:
            return False  
    else:
        return False 
 
# 5 - Sum of odd numbers
def row_sum_odd_numbers(n):
    return n ** 3
 