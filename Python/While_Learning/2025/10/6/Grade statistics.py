def grade_stat(dict):
    for key in dict:
        a = dict[key][0]
        b = dict[key][1]
        c = dict[key][2]
        dict[key] = (a+b+c)/3
    return dict
    
dict = {'Alice':(88, 99, 87), 'Shu':(100, 99, 98)}
print(grade_stat(dict))