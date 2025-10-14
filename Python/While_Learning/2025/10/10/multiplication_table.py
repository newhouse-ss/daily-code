numbers = [-3, -2, -1, 0, 1, 2, 3]

posi_nums = [x for x in numbers if x > 0]
print(posi_nums)

words = ["apple", "banana", "cherry"]
upper_words = [x.upper() for x in words]
print(upper_words)

sentence = "This is a test sentence"
len_of_words = [len(x) for x in sentence.split()]
print(len_of_words)

