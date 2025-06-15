#find the maximun sum of k cards that should be take from first or last
a=[4,2,7,20,8,6,8,1]
k=3
n=len(a)
sums=0
for i in range(k):
    sums+=a[i]
maxi=sums
l=k-1
r=len(a)-1
m2=sums
for i in range(k-1,0,-1):
    m2-=a[l]
    m2+=a[r]
    maxi=max(maxi,m2)
    l-=1
    r-=1
print(maxi)
    
    