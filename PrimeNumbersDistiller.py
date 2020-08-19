def solution(n):
    if (0 <= n < 10000):
        i = 2
        primeStr = ''



        while len(primeStr) < 10005:
            isPrime = True;
            for j in range (1,i+1):
                if i % j == 0 and (j != 1 and j != i):
                    isPrime = False
            if isPrime:
                primeStr+=str(i)
            i+=1


        return primeStr[n:n+5]
    else:
        return None


primeList = solution(0)
# print(len (primeList))
print(primeList)





