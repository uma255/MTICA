spins = [('red','18'),('black','13'),('red','7'),('red','18'),('black','13'),('red','25'),('red','2'),('black','26'),('black','31'),('red','3')]
def countreds(aList):
    count=0
    for color,number in aList:
        if color =='black':
            yield count
            count=0
        else:
            count +=1
    yield count
gaps=[gap for gap in countreds(spins)]
print(gaps)
