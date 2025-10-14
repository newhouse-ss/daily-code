dic = [{'name':'Alice', 'score':88}, {'name':'Shu', 'score':98}, {'name':'Ken', 'score':55}]
sorted_dic = sorted(dic, key = lambda item : item['score'], reverse=True)
print(sorted_dic)