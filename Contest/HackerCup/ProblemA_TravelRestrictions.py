def travel(n,I,O):
    l1=[]
    #print(I,O)
    for i in range(n):
        l4=[]
        for j in range(n):
            if i==j:
                l4.append(1)
            else:
                l4.append(0)
        l1.append(l4)
    #print(l1)
    #print(l1[0].index(1))
    for out in range(n):
        incoming=out
        outgoing=out
        while(incoming!=0):
            incoming-=1
            #print(outgoing,incoming,O[outgoing],I[incoming])
            if O[outgoing]=='Y' and I[incoming]=='Y':
                l1[out][incoming]=1
                outgoing-=1
            else:
                break
    #print(l1)
    for out in range(n):
        incoming=out
        outgoing=out
        while(incoming!=(n-1)):
            incoming+=1
            #print(outgoing,incoming,O[outgoing],I[incoming])
            if O[outgoing]=='Y' and I[incoming]=='Y':
                l1[out][incoming]=1
                outgoing+=1
            else:
                break
    #print(l1)
    for i in range(n):
        for j in range(n):
            if l1[i][j]==1:
                print('Y',end="")
            else:
                print('N',end="")
        print()

t=int(input())
for i in range(t):
    n=int(input())
    I=input()
    I=list(I)
    O=input()
    O=list(O)
    print("Case #",i+1,":",sep="")
    travel(n,I,O)