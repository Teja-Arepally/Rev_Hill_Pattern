def rev_hill(n):
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(i,n-1):
            print("*",end=" ")
        for j in range(i,n):
            print("*",end=" ")
        print()
rev_hill(5)                   