import math
def checkPronic (x) :
    i = 0
    while ( i <= (int)(math.sqrt(x)) ) :
        if ( x == i * (i + 1)) : 
            return True
        i = i + 1
    return False

string = input()
res = [string[i: j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]
returner = []
for i in res:
	if checkPronic(int(i)):
		returner.append(int(i))

returner.sort()
store = set()
if len(returner) == 0:
	print("-1")
	exit()
for i in range(len(returner)-1):
	if returner[i] not in store and returner[i]!=0:
		store.add(returner[i])
		print(returner[i], end=",")
print(returner[len(returner)-1])
