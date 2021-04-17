def isp(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "*", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")


def numofprime(a, b):
    primenumbers = []
    for num in range(a, b+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primenumbers.append(num)
    print(primenumbers)


while True:
    print('1- check prime number')
    print('2- find prime numbers between two number')
    print('3- exit')
    choice = int(input('choose what do you want?: '))
    if choice == 1:
        num = int(input("Enter a number: "))
        isp(num)
    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        numofprime(a, b)
    elif choice == 3:
        exit()
    else:
        print('Enter correct option from menu')
