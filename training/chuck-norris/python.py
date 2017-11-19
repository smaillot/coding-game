o=""
l=""
b = ''.join(list(map(lambda x:"{:07b}".format(ord(x)),list(input()))))
for c in b:
    if c!=l:
        o+=' '+'0'*(2-int(c))+' '
        l=c
    o+='0'
print(o[1:])
