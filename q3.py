def wordCount(t):
    word_dict = {}
    with open(t, 'r') as file:
        for line_num, line in enumerate(file, start=1): # iterate through each line, keeping track with enumerate
            words = line.strip().split() # seperate the words in the line
            for word in words:
                if word not in word_dict:
                    # if the word is not in the dictionary, add it as 
                    # as the key, with the line number being the value
                    word_dict[word] = [line_num] 
                else:
                    # if the word exists, append the line number
                    # to the word, where the key is the word
                    word_dict[word].append(line_num)
    return word_dict

def main():
    print(wordCount("q3test.txt")) # print the dictionary

if __name__ == "__main__":
    main()