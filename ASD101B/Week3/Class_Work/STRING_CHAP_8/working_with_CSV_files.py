

def main():

    csv_file = open(r'C:\Users\markh\OneDrive\Documents\Mark_Python_Files\ASD101B\Week3\Class_Work\CSV_FILES\test_scores.csv', 'r')

    lines = csv_file.readlines()
    csv_file.close()

    for line in lines:
        tokens = line.split(',')
        total = 0.0
        for token in tokens:
            total += float(token.strip())

        average = total / len(tokens)
        print(f'Average: {average}')

    
    print(lines)


if __name__ == '__main__':
    main()
