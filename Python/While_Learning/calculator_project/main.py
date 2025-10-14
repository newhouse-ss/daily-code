from calculator.arithmetic import add

def main():
    """主函数，程序的执行入口。"""
    print("--- 欢迎使用计算器程序 ---")

    # --- 演示算术运算 ---
    print("\n--- 算术运算 ---")
    num1 = 20
    num2 = 10
    
    sum_result = add(num1, num2)
    print(f"{num1} + {num2} = {sum_result}")

if __name__ == "__main__":
    main()

