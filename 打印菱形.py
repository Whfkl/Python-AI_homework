for i in range(9):
    for j in range(9):
        if(abs(i-4)+abs(j-4) == 4):
            print("*",end="")
        else:
            print(" ",end = "")
    print("")
