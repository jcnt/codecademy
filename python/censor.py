def censor(text, word):
    list = text.split()
    endlist = []
    for i in list: 
        if i == word:
            endlist.append("*" * int(len(i)))
        else:
            endlist.append(i)
    return " ".join(endlist)
        
    
censor("bela elment a boltba", "bela")


