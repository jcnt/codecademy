def median(inlist):
    slist = sorted(inlist)
    print slist
    if len(inlist) % 2 == 0:
        emid = len(slist) / 2
        return (float(slist[emid-1]) + float(slist[emid]))/2
    if len(inlist) % 2 == 1:
        return len(slist) / 2
        

median([1,2,3,4,5])

