string='''practice problmes for list com pre hension in python.'''

wordslst=string.split(' ')
print(wordslst)
wordlst=[i.strip("\n") for i in wordslst]
print(wordslst)
#ans=(word:len(word) for word in wordslist )
ans={i:len(i) for i in wordslst }
print(ans)
