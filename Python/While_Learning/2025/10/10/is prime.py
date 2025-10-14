def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num%2 == 0:
        return False
    i = 3
    while i*i <= num:#如果i*i>num, 那么i不可能被num整除, 因为整除的结果必须>=2
        if num%i == 0:
            return False
        i += 1
    return True

def main():
    list_prime = [x for x in range(20) if is_prime(x)]
    print(list_prime)

if __name__ == '__main__':
    main()