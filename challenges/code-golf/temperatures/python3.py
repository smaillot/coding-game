n=int(input())
t=list(map(int,input().split()))
a=[abs(e)for e in t]
m=[t[e]for e in[i for i,x in enumerate(a)if x==min(a)]]
if n!=0:r=max(m)
else:r=0
print(r)
