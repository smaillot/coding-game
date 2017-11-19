# given a conversion table from hex to a 2 letters syllable
# convert a decimal number input a word

n = hex(int(input()))[2:]

a=’HBKD’
b=’OAEI’

def conv(n):
    x=int(n,16)
    return(a[x//4]+b[x%4])

print(''.join([conv(i) for i in n]))
