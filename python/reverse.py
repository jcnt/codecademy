def reverse(word):
    drowl = []
    for i in range(len(word)):
        drowl.append(word[(len(word)-i-1)])
    drow = "".join(drowl)
    print drow
    	

reverse('longword')
