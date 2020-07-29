n=int(input())
bride=input()
groom=input()
while(len(bride)>0):
    flag=0
    j=0
    while(len(groom)>0):
        if j==len(groom):
            break
        if bride[0]==groom[0]:
            #print("here1")
            bride = bride[1:]
            groom = groom[1:]
            flag=1
            break
        else:
            #print("here2")
            j+=1
            groom = groom[1:] + groom[0]
    if flag==0:
        break
print(len(bride), end='')