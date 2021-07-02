import string
def articleLenght(word):
    return len(word)

def firstLetter(word):
    return ord(word[0])-97

def primeNumber(word):
    isPrime = True
    sum = 0
    for character in word:
        number = ord(character) - 96
        index = 2
        quantity = 0
        while quantity!=number:
            isPrime = True
            for i in range(index//2+1):
                if i==0 or i==1: 
                    continue
                if index%i==0:
                    isPrime = False
                    break
            if isPrime:
                quantity+=1
            index+=1
        sum+=index-1
    return sum%10


if __name__ == '__main__':
    print(primeNumber('apple'))
    print(primeNumber('darslik'))
    print(primeNumber('dorixona'))
    print(primeNumber('mohirdev'))