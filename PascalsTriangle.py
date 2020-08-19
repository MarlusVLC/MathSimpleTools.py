from math import factorial

def PascalsTriangle (deg):
    if (deg == 0):
        return 1
    expanBin = []
    for i in range(deg):
        expanBin.append(int(factorial(deg)/factorial(i)*factorial(deg-i)))
    return tuple (expanBin)

print (PascalsTriangle(2))



