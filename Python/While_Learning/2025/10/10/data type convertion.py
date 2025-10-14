def convert_string_to_number(str):
    cleaned_string = str.strip()

    if not cleaned_string:
        print("Input is empty.")
        return None
    
    try:
        conv_int = int(cleaned_string)
        print("Int type")
    except ValueError:
        try:
            conv_float = float(cleaned_string)
            print("Float type")
        except ValueError:
            print("Not a valid number.")
            return None

def main():
    test_cases = [
        "12345",       # Valid integer
        "   -50   ",  # Valid integer with whitespace
        "98.76",       # Valid float
        "hello world", # Invalid string
        "1.0.0",       # Invalid float format
        "",            # Empty string
        "1,000"        # Invalid (contains a comma)
    ]
    for tester in test_cases:
        print('-'*30)
        print(f"Tester is: {tester}")
        convert_string_to_number(tester)

if __name__ == '__main__':#只有当把脚本直接运行时才会这样赋值，如果脚本被当作module导入，则会把module名给__name__，则不会执行以下的部分。
    main()