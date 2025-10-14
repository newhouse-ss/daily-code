import datetime
import os

# --- task1: design Entry class ---
class Entry:
    """Denote a item in the diary book"""
    def __init__(self, content):#Do not need to afford the timestamp as argument, it will be aquired by datetime module.
        """
        Initialize a diary entry.
        Args:
            content(str): Content of diary
        """
        self.content = content
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        """
        return the entry as string
        Returns:
            str: String with format:[YYYY-MM-DD HH:MM:SS] content.
        """
        return f"{self.timestamp.strftime("%Y-%m-%d %H-%M-%S")}\n{self.content}"#将时间戳格式化

# --- 任务 2: 设计 Diary 类 ---
class Diary:
    """管理所有日记条目。"""
    def __init__(self):
        """初始化一个空的日记本。"""
        self.entries = []  # 这个列表用来存放所有的 Entry 对象，想要修改的话试试用字典来存吧。

    def add_entry(self, content):
        """
        向日记本中添加一个新的条目。
        Args:
            content (str): 新日记的内容。
        """
        print("正在添加新日记...")
        new_entry = Entry(content)
        self.entries.append(new_entry)

    def show_entries(self):
        """打印出所有的日记条目。"""
        if not self.entries:
            print("日记本是空的。")
        else:
            print("--- 日记列表 ---")
            for entry in self.entries:
                print(entry)
            print("----------------")

    def save(self, filename="diary.txt"):
        """
        将所有日记条目保存到文件中。
        Args:
            filename (str): 要保存的文件名。
        """
        print(f"正在保存日记到 '{filename}'...")

        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for entry in self.entries:
                    file.write(str(entry) + '\n')
                print("保存成功！")
        except Exception as e:
            print(f"Can not open the file, reason: {e}")


    def load(self, filename="diary.txt"):
        """
        从文件中加载日记条目。
        
        Args:
            filename (str): 要加载的文件名。
        """
        print(f"正在从 '{filename}' 加载日记...")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.entries = [] # 清空现有日记，因为马上要从txt file中load内容，所以可以放心清空，open(filename, "w")， 也可以用w-mode
                for line in file:
                    content_from_file = line.strip() 
                    if content_from_file: # 确保不是空行
                        entry = Entry(content_from_file)
                        self.entries.append(entry)
            print("加载成功！")
        except FileNotFoundError:
            print(f"文件 '{filename}' 未找到。")


# --- 任务 3: 构建主程序逻辑 ---
def main():
    """程序的主循环和交互逻辑。"""
    my_diary = Diary()    
    my_diary.load()#如果diary.txt中有内容的话，在这一步会被全部load到self.entries中

    while True:
        print("\n--- 命令行日记本 ---")
        print("1. 添加日记")
        print("2. 查看所有日记")
        print("3. 保存日记")
        print("4. 退出")

        choice = input("请输入你的选择: ")
        if choice == '1':
            content = input("Begin to write: ")
            my_diary.add_entry(content)
        elif choice == '2':
            my_diary.show_entries()
        elif choice == '3':
            my_diary.save()
        elif choice == '4':
            my_diary.save()
            print("The content is saved automately.")
            break
        else:
            print("Input the right option.")

if __name__ == "__main__":
    main()