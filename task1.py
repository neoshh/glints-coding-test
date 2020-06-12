def markedAsAdj(hdb, x, y):
    if x < 0 or x >= len(hdb) or y < 0 or y >= len(hdb[x]) or hdb[x][y] == "0":
        return
    hdb[x][y] = "0"
    markedAsAdj(hdb, x - 1, y)
    markedAsAdj(hdb, x + 1, y)
    markedAsAdj(hdb, x, y + 1)
    markedAsAdj(hdb, x, y - 1)
    markedAsAdj(hdb, x - 1, y - 1)
    markedAsAdj(hdb, x + 1, y + 1)
    markedAsAdj(hdb, x - 1, y + 1)
    markedAsAdj(hdb, x + 1, y - 1)

def findClusters(hdb):
    num = 0
    for x in range(len(hdb)):
        for y in range(len(hdb[x])):
            if hdb[x][y] == "+":
                num += 1
                markedAsAdj(hdb, x, y)
    return num

hdb1 = [['0','0','0','+','+','0'], 
        ['+','+','+','0','0','+'], 
        ['0','0','0','0','0','0'], 
        ['+','0','0','0','0','+'], 
        ['+','+','0','0','+','0']]

hdb2 = [['0','+','0'], 
        ['+','0','+'], 
        ['0','+','+']]

print(findClusters(hdb1))    # prints 3
print(findClusters(hdb2))    # prints 1
