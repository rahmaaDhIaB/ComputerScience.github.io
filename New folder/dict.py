def letter_count(word):
    dictionary = {}
    for i in word:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    return dictionary
        

def invert(d):
    Copies = []
    NewDickt = {}
    for i in d:
        Copies.append(i)
    

    for j in Copies:
        value = d[j]
        NewDict[value]=j