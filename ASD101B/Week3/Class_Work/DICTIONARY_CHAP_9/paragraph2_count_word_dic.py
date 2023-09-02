

def paragraph2():

    file_path = r'C:\Users\markh\OneDrive\Documents\Mark_Python_Files\ASD101B\Week3\Class_Work\STRING_CHAP_8\TEXT_FILES\paragraph2.txt'

    with open(file_path, 'r') as myFile:
        readFile = myFile.read()
        fileLst = readFile.split()
        newCleanLst = []

        for word in fileLst:
            cleanWrd = ''.join(filter(str.isalnum, word)).lower()
            newCleanLst.append(cleanWrd)

       
        word_count = {}  # Initialize an empty dictionary to store word counts

        for word in newCleanLst:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        sorted_word_count = dict(sorted(word_count.items()))
        

    for word, count in sorted_word_count.items():
        print(f'{word}: {count}')

   
    myFile.close()

if __name__ == '__main__':
    paragraph2()
