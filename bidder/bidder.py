def getUnallottedUsers(bids, totalShares):
    curShares = totalShares
    byPrice = {}
    empID = set()
    for bid in bids:
        empID.add(bid[0])
        if bid[2] not in byPrice.keys():
            byPrice[bid[2]] = []
        byPrice[bid[2]].append(bid)
    for price in sorted(byPrice.keys(),reverse=True):
        if totalShares <= 0: break 
        if len(byPrice[price]) == 1:
            curShares -= price
            if byPrice[price][0][0] in empID: empID.remove(byPrice[price][0][0])
        else:
            while curShares > 0 and len(byPrice[price]) > 0:
                for bid in :
                    bid[1] -= 1
                    curShares -= 1
                    if bid[0] in empID: empID.remove(bid[0])
                byPrice[price].remove(bid)


    return empID
            
        


print(
    getUnallottedUsers(
    [
        [1, 2, 5, 0],
        [2, 1, 4, 2],
        [3, 5, 4, 6],
    ],
    3
    )
)


x = [1,2,3]
for y in x:
    if y == 2:
        x.remove(y)
print (x)