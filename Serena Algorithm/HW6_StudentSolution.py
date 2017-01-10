from operator import itemgetter
def HW6_StudentSolution(rallies):
    final = []
    finaler = []
    myDict = {}
    count = 0
    for x in rallies:
        final.append((count,x[1]))
        myDict[x[1]] = x[0]
        count = count + 1
    final = sorted(final,key=itemgetter(1))
    accum = 0
    count = 0
    for y in final:
            finalTuple = (y[0],accum)
            accum = accum + myDict[y[1]]
            finaler.insert(count, finalTuple)
            if accum > y[1]:
                return []
            count = count + 1
    return finaler
