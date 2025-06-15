a=[2,1,1,2,3,1,1]
f={}
for i in a:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1
for i in f:
    if f[i]>len(a)/2:
        res=i
print(res)
#-------------------------------------------------or (boyer more algo)------------------------------------------------------

r=m=0
for i in a:
    r=i
    if i==r:
        m+=1
    else:
        m-=1
print(r)
#----------------------------------------------or--------------------------------------------------------

c=1
res=a[0]
for i in range(1,len(a)):
    if res==a[i]:
        c+=1
    else:
        c-=1
        if c==0:
            res=a[i]
            c=1
print(res)