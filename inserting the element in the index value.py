#print the mid value if target is found  else print the index where the target should be inserted

a=[2,4,6,7,8,10,13,15]
x=6
l=0
r=len(a)-1
res=-1
while l<=r:
    mid=(l+r)//2
    if a[mid]==x:
        res=mid
        break
    elif x<a[mid]:
        r=mid-1
    else:
        l=mid+1
if res!=-1:
    print(res)
else:
    print(l)