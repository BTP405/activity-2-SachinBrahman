import matplotlib.pyplot as plt

def graphSnowfall(t):
    snowfall_ranges = [0, 10, 20, 30, 40, 50]
    snowfall_counts = [0, 0, 0, 0, 0]

    with open(t, 'r') as file:
        for line in file:
            snowfall = int(line.strip())
            for i in range(len(snowfall_ranges) - 1):
                # check which range the snowfall falls into and increment the count
                if snowfall_ranges[i] < snowfall <= snowfall_ranges[i + 1]:
                    snowfall_counts[i] += 1
                    break

    x_labels = ['0-10cms', '10-20cms', '20-30cms', '30-40cms', '40-50cms']
    x = range(len(x_labels))

    plt.bar(x, snowfall_counts, tick_label=x_labels)
    plt.xlabel('Snowfall Ranges')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Distribution')
    plt.show()

def main():
    graphSnowfall("q2test.txt")

if __name__ == '__main__':
    main()