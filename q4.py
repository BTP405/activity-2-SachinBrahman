def printStats(t):
    def decorator(func):
        with open(t, 'r') as file:
            for line in file:
                numbers = list(map(int, line.strip().split())) # create a list of the integers in the line
                print("Numbers read:", numbers)
                print("Count:", len(numbers))
                print("Average:", sum(numbers) / len(numbers))
                print("Maximum:", max(numbers))
                print("-------------------------------")
        return func
    return decorator

@printStats("q4test.txt")
def main():
    pass

if __name__ == "__main__":
    main()