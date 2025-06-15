a=list(map(int,input().split()))
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[j]<a[i]:
            a[i],a[j]=a[j],a[i]
print(a)
#######################################################################################################

#bestcase
a=[4,7,8,3,5,1]
c=0
k=3
for j in range(len(a)-1):
    f=False
    for i in range(len(a)-1-j):
        c=c+1
        if(a[i]>a[i+1]):
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if f==False:
        break
print(a[-k])
print(c)

            