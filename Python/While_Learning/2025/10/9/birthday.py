import datetime

def calculate(birth_day):
    today = datetime.date.today()
    age = today.year-birth_day.year-((today.month, today.day) < (birth_day.month, birth_day.day))

    return age

birth_day = datetime.date(2002, 2, 15)
print(calculate(birth_day))