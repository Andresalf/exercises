EMPTY_CELL = '-'

def place_words(crossword, words, start, words_used):
    pass

words = ['LONDON', 'DELHI', 'ICELAND', 'ANKARA']
words_used = set()
crossword = []
crosswordFile = open('crossword.txt', 'r')
for line in crosswordFile:
    rowList = []
    for ch in line[:-1]:
        rowList.append(ch)

    crossword.append(rowList)

crosswordFile.close()

start = None
for i, row in enumerate(crossword):
    for j, chr in enumerate(row):
        if chr == EMPTY_CELL:
            start = i, j


place_words(crossword, words, start, words_used)