def leap_year_checker(year):
    a = year%4
    b = year%100
    c = year%400
    if (a == 0 and b!=0) or c == 0:
        return True
    else:
        return False
    
print(leap_year_checker(200))