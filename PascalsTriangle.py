from math import factorial


class PascalsTriangle:

    def graphicRep (self, deg):
        if (deg == 0):
            return 1
        expanBin = []
        for i in range(deg):
             expanBin.append(int(factorial(deg)/factorial(i)*factorial(deg-i)))
        return tuple (expanBin)


pasc = PascalsTriangle()

print(pasc.graphicRep(2))





