a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6]]
c = [[1, 2], [3, 4], [5, 6]]
def printList(a):
    for item in a:
        print(" ".join(map(str,item)))

def transportMatrix(a):
    result = list()
    rows = len(a)
    colls = len(a[0])    
    for i in range(0, colls):
        temp = list()
        for j in range(0, rows):
            temp.append(a[j][i])
        result.append(temp)
    return result
        
printList(a)
print()
result = transportMatrix(a)
printList(result)
print()

printList(b)
printList(transportMatrix(b))
print()

printList(c)
printList(transportMatrix(c))
