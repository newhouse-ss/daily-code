db = [
    ("John Doe", 30, "New York"),
    ("Shu", 23, "Tokyo"),
    ("SARA", 23, "Tokyo"),
]

def search_items(db_name):
    topic = input("Input the item you want to search for(name/age/city): ")
    if topic == 'name':
        name = input("Give the name you want to search")
        for item in db_name:
            if item[0] == name:
                print(item)
    elif topic == 'age':
        try:
            age = int(input("Give the age you want to search"))
            for item in db_name:
                if item[1] == age:
                    print(item)
        except ValueError:
            print("Just give me the right number.")
    elif topic == 'city':
        city = input("Give the city you want to search")
        for item in db_name:
            if item[2] == city:
                print(item)

search_items(db)