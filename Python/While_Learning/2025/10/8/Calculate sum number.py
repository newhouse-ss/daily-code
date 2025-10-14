'''
def calcu_sum_num(filename):
    num = 0
    try:
        with open(filename, 'r') as file:
            try:  #这里的try和下一层的while之间的嵌套关系出错了，这样的话只要while中有一个非数字就会except
                line = file.readline()
                while line:  #而我想要的是在每一行中判断一下是否是数字。
                    line = file.readline()
                    if line.strip().isinstance(int):
                        num += 1
                    else:
                        line = int(line)
                        num += 1
            except ValueError:
                print("Something could not be transfored to int type.")
                print(num)
    except FileNotFoundError:
        print("No such file.")

        calcu_sum_num('numbers.txt')
'''
def calcu_sum_num_2(filename):
    total = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    total += 1
                except ValueError:
                    print(f"This line could not be transformed to int: {line}")
            return total
    except FileNotFoundError:
        print("No such file.")
        return None
    finally:#但是使用with打开文件的时候就不再需要finally
        if 'file' in locals() and file:
            file.close()
            print("App files are closed.")
print(calcu_sum_num_2('numbers.txt'))