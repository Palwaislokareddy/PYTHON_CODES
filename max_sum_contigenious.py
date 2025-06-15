#print the max sum of the k contigenious elements
# subarray:[2,1,6,4]
# subsequence:[2,3,4,6]
a=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=5
sum1=sum(a[:k])
maxi=sum1
for i in range(k,len(a)):
    sum1=sum1-a[i-k]+a[i]
    if sum1>maxi:
        maxi=sum1
print(maxi)
#--------------------------------------------------------------
maxi=0
for i in range(len(a)-1):
    sum1=sum(a[i:k])
    if maxi<sum1:
        maxi=sum1
    k=k+1
    i+=1
print(maxi)
#-----------------------------------------------------------------------
a=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=5
m=0
for i in range(0,len(a)-k+1):
    r=i+k
    sums=sum(a[i:r])
    m=max(m,sums)
print(m)