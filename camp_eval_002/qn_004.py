def floyd(n):
    i,j,k=1,1,1
    while(i<=n):
        while(j<=i):
            if k<10:
                print('0'+str(k),end=" ")
            else:
                print(str(k),end=" ")
            k+=1
            j+=1
        print()
        i+=1
        j=1
        
floyd(10)
