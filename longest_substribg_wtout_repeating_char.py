#longest substring without repeating chars
a="abcdcecdb"
'''
l=0
r=0
maxi=0
while r<len(a):
    stri=a[l:r+1]
    d=sorted(stri)
    e=sorted(set(stri))
    if len(set(stri))==len(stri) and d==e :
        maxi=max(maxi,r-l+1)
        r+=1
    else:
        l+=1
print(maxi)'''

#----------------------------------------or----------------------------------------------
#in dicta
a="abcdecfbgce"
d={}
l=0
m=0
start=0
for r in range(len(a)):
    if a[r] not in d:
        d[a[r]]=r
    else:
        if d[a[r]]>=l:
            l=d[a[r]]+1
        d[a[r]]=r
    if r-l+1>m:
        m=r-l+1
        start=l
    m=max(m,r-l+1)
print(m,a[start:start+m])
    
        
    
