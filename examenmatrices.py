matriz=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
for i in range(0, 4):
    sumador=0
    if i%2==0:
        fcor j in range(0, 3, 2):
            sumador+=matriz[i][ j]
    else:
        for j in range(1, 5, 2):
            sumador+=matriz[i][ j]
    print(sumador)
