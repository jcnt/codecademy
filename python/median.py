def median(inlist):
    slist = sorted(inlist)
    print slist
    if len(inlist) == 1:
        return inlist[0]
    if len(inlist) % 2 == 0:
        emid = len(slist) / 2
        return (float(slist[emid-1]) + float(slist[emid]))/2
    if len(inlist) % 2 == 1:
        print slist
        return slist[(len(slist) / 2)]
        

median([6, 8, 12, 2])

