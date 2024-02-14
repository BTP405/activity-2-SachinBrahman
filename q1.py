def getPrimeNumbers(n):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False # if num is divisible by any number between 2 and itself, return false
        return True # else return true

    # iterate through 2 to the num given, is isPrime returns true, add the number to the list
    return [num for num in range(2, n + 1) if isPrime(num)]

def main():
    print(getPrimeNumbers(50))

if __name__ == "__main__":
    main()