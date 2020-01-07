def reverse(x):
    return x[::-1]
def horizontal(input,words):
    flag=0
    for i in range(len(input)):
        for j in range(len(input)):
            word=input[i][j].lower()
            max=len(words)-1
            k=j+1
            while(max>0):
                #print(word)
                if(k<len(input)):
                    word+=input[i][k].lower()
                    #print(word)
                    if(word==words):
                        print("Element",words,"found at",i,'th row',j,'th column','to',i,'th row',k,'th column')
                        flag=1
                    elif(word==reverse(words)):
                        print("Element", words, "found at", i, 'th row', k, 'th column', 'to', i, 'th row', j,'th column')
                        flag = 1
                k+=1
                max-=1
    return flag
def vertical(input,words):
    flag=0
    for i in range(len(input)):
        for j in range(len(input)):
            word = input[j][i].lower()
            max=len(words)-1
            k=j+1
            #print(word)
            while (max > 0):
                #print(word)
                if (k < len(input)):
                    word += input[k][i].lower()
                    #print(word)
                    if (word == words):
                        print("Element", words, "found at", i, 'th row', j, 'th column', 'to', i, 'th row', k,
                              'th column')
                        flag = 1
                    elif(word==reverse(words)):
                        print("Element", words, "found at", i, 'th row', k, 'th column', 'to', i, 'th row', j,'th column')
                        flag=1
                k += 1
                max -= 1
    return flag

def diagonal(input,words):
    flag=0
    for i in range(len(input)):
        for j in range(len(input)):
            word = input[i][j].lower()
            max = len(words) - 1
            l=1
            #k = j + 1
            while (max > 0):
                if (i+l<len(input) and j+l<len(input)):
                    word += input[i+l][j+l].lower()
                    #print(word)
                    if (word == words):
                        print("Element", words, "found at", i, 'th row', j, 'th column', 'to', i+l, 'th row', j+l,'th column')
                        flag = 1
                    elif(reverse(words)==word):
                        print("Element", words, "found at", i+l, 'th row', j+l, 'th column', 'to', i , 'th row', j ,'th column')
                        flag = 1
                l+= 1
                max -= 1
    return flag
def diagonal_1(input,words):
    flag = 0
    for i in range(len(input)):
        for j in range(len(input)-1,-1,-1):
            word = input[i][j].lower()
            max = len(words) - 1
            l = 1
            # k = j + 1
            while (max > 0):
                if (i + l < len(input) and j - l < len(input)):
                    word += input[i + l][j - l].lower()
                    #print(word)
                    if (word == words):
                        print("Element", words, "found at", i, 'th row', j, 'th column', 'to', i + l, 'th row', j -l,
                              'th column')
                        flag = 1
                    elif (reverse(words) == word):
                        print("Element", words, "found at", i + l, 'th row', j -l, 'th column', 'to', i, 'th row', j,
                              'th column')
                        flag = 1
                l += 1
                max -= 1
    return flag
#MAIN FUNCTION
words=input()
max=len(words)
input=[
  ["P", "S", "U", "W", "H", "A", "T", "S"],
  ["L", "P", "A", "C", "K", "A", "G", "E"],
  ["N", "Y", "O", "L", "R", "D", "V", "L"],
  ["F", "I", "N", "G", "E", "Z", "B", "M"],
  ["I", "R", "E", "H", "Q", "N", "J", "O"],
  ["A", "T", "B", "V", "G", "Y", "E", "S"],
  ["J", "D", "U", "W", "U", "E", "S", "T"],
  ["P", "S", "T", "I", "C", "K", "E", "Y"]
]
flag=0
flag=horizontal(input,words)
if(flag==1):
    exit()
flag=vertical(input,words)
if(flag==1):
    exit()
flag=diagonal(input,words)
if(flag==1):
    exit()
flag=diagonal_1(input,words)
if(flag==1):
    exit()
print("Not found")
