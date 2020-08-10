import collections
arrSize, k = list(map(int, input().split()))
arr = collections.Counter(map(int, input().split()))
# print(arr)
hitesh_saini = set()
for elem in arr:
    hitesh_saini.update((elem-i for i in range(1,k+1)))
    hitesh_saini.update((elem+i for i in range(1,k+1)))
    # print(hitesh_saini)

filterer = collections.Counter()
filterer.update(dict.fromkeys(hitesh_saini, float("inf")))
print(filterer)
print(arr)
totals = sum((arr & filterer).values())
print(totals)