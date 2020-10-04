def solve(a,b,c,d,e):
  cost= ((d/a)*b + e)*60 + c
  return cost
  
a1=int(input())
b1=int(input())
c1=int(input())
d1=int(input())
e1=int(input())
a2=int(input())
b2=int(input())
c2=int(input())
d2=int(input())
e2=int(input())
res1=solve(a1,b1,c1,d1,e1)
res2=solve(a2,b2,c2,d2,e2)
print("petrol" if res1<res2 else "diesel", end="")