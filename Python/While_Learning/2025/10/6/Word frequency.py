def word_frequency(text):
    text.lower()
    text = ''.join(c for c in text if c.isalnum() or c.isspace())#最关键的一点，如何通过comprehension使句子只包含字母、数字和空格。
    print(text)
    text = text.split(' ')
    dictionary = {}
    for word in text:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary

feeling = 'I want to know how to escape from anxiety and loneliness'
print(word_frequency(feeling))