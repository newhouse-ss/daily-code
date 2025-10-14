def vowel_skipper(stg):
    vowel = ["a",'e','i','o','u','A','E','I','O','U']
    for char in stg:
        if char in vowel:
            continue
        else:
            print(char)

string = 'I am so painful!'
vowel_skipper(string)