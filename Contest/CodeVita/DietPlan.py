n, k = map(int, input().split())
arr = list(map(int,input().strip().split()))[:n]

count=0
for i in range(0,n):
  strt=arr[i]-k
  en=arr[i]+k
  for j in arr:
    if(j!=arr[i]):
      if(j>=strt and j<=en):
        count=count+1
        break
print(count)