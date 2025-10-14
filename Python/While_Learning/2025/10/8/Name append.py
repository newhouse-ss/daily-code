new_users = ['Alice', 'Shu', 'Leon']
file_name = 'user_table.txt'
try: 
    with open(file_name, 'a') as file:
        for user in new_users:
            file.write(user+'\n')
except Exception:
    print("Something wrong.")