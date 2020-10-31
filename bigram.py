import re
file = open('clean_data_blankline_remove_final.txt', 'r', encoding='utf-8')
bigram_output = open('bigram_input.txt', 'w', encoding='utf-8')
f = file.readlines()

newList = []
for line in f:
    if line[-1]=='\n':
        newList.append(line[:-1])
    else:
        newList.append(line)
#print(newList)
length = len(newList)
print(length)
i = 0

while i < (length-1):
    j = i + 1
    bi_string = newList[i] + " " + newList[j]
    #print(bi_string)
    bigram_output.write(bi_string)
    bigram_output.write('\n')
    i+=1




