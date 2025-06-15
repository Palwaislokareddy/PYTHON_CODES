n=int(input())
r=int(input())
s=n-r
rfact=nfact=sfact=1
for i in range(1,n+1):
    nfact*=i
print(nfact)
for i in range(1,r+1):
    rfact*=i
print(rfact)
for i in range(1,s):
    sfact*=i
total=nfact/(rfact*sfact)
print(int(total))
    
    