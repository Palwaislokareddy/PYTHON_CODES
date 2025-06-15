# finding the longest non repeating character substring and the x any y value should present in the string
a="abcedacefaebghd"
d={}
l=0
m=0
start=0
x='c'
y='d'
for r in range(len(a)):
    if a[r] not in d:
        d[a[r]]=r
    else:
        if d[a[r]]>=l:
            l=d[a[r]]+1
        d[a[r]]=r
    curr=a[l:r+1]
    print(curr)
    if x in curr and y in curr:
        if r-l+1>m:
            m=r-l+1
print(m,a[start:start+m])
    