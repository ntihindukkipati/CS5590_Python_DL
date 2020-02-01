infile = open("scratch.txt",'r')
wordsCount = dict()
for line in infile:
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word in wordsCount:
            wordsCount[word] = wordsCount[word]+1
        else:
            wordsCount[word] = 1

print (wordsCount)