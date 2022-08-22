start=1
end=6
for i in range(start, end):
    for k in range(1,end-i):
        print(" ",end="")
    for j in range(0,2*i-1):
        if j==0:
            print(1,end="")
        print(j, end="")
    print(end="\n")
