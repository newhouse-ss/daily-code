from script1 import *#这样导入的时候如果因为被导入module作者的疏忽没有写main()函数运行条件，会发生unintended的情况，所以尽量导入确切的东西

def food(food):
    print(f"This is the script2 food.{food}")

def main():
    print("This is main() of script2.")

main()#说明script1中的main()函数也会被导入，但是如果在本module中也定义main()的话，script1中的main()则会被覆盖。