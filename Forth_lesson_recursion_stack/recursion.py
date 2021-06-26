def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return factorial(num-1)*num

if __name__ == '__main__':
    print(factorial(10))
