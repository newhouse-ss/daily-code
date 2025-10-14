string = 'Compute the unique words in this sentence, you are asked to remove the repeated word(s).'
set_of_string = set(string.split())#不能再还原成原来的句子了，因为set里面的元素没有次序。
print(set_of_string)
print(len(set_of_string))