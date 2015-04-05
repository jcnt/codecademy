def digit_sum(n):
    sumi = 0
    for i in range(len(str(n))):
        sumi = sumi + int(str(n)[i])
    print "The sum of the numbers is %i" % sumi

x = int(raw_input("please enter a number: "))
digit_sum(x)
