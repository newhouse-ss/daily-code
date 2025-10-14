def greeting():
    print("Hello!")
def food(food):
    print(f"Your favorite food is: {food}")

#但是我不想在将本module中的函数导入其他module时执行以下部分！！！！
def main():
    greeting()
    food("peach")

if __name__ == '__main__':
    main()

#当使用from script1 import *想要把当前module中的所有东西导入另一个module的时候，运行到第十一行的时候会检查当前模块的__name__，如果是被导入的情况
#__name__ == "__main__", 所以本模块的main()就不会被包含在导入的部分中，用于保护被导入module中不想被执行的代码。