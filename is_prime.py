def is_prime(num: int) -> bool:
    for i in range(2,num):
        if (num % i == 0):
            flag = False
            break
        else: flag = True
    return flag

def main():
    print(is_prime(int(input('number: '))))

if __name__ == '__main__':
    main()