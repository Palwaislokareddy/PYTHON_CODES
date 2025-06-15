a=[4,4,4,2,1,2,2,1,4,4,3]
l=0
d={}
m=0
for r in range(len(a)):
    if a[r] not in d:
        d[a[r]]=1
    else:
        d[a[r]]+=1
    if len(d)>2:
        d[a[l]]-=1
        if d[a[l]]==0:
            del d[a[l]]
        l+=1
    if len(d)<=2:
        m=max(m,r-l+1)
print(m)
