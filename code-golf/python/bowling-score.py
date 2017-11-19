# read bowling score sheet
d={'X':30,'/':20,'-':0}
e={}
for i in range(int(input())):
  a, p, q = input().split()
  e[(int(p) if p not in d else d[p]) + (int(q) if q not in d else d[q])] = a
  print(e[max(e)])
