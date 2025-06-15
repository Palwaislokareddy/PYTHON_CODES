#max length of the subarray whose sum is less than or equal to the k value
a=[2,1,4,6,2,3,1,1,4,2,6,7,3]
k=7
'''length=0
count=0
for i in range(len(a)-1):
    curr=0
    for j in range(i,len(a)):
        curr+=a[j]
        if curr<=k:
            length=max(length,j-i+1)
            count+=1
        else:
            break
print(length,count)'''

#-----------------------------------------------or-------------------------------------------
l=0
r=0
k=7
maxi=0
sum1=0
while r<=len(a):
    sum1=sum(a[l:r])
    if sum1<=k:
        maxi=max(maxi,len(a[l:r]))
        r+=1
    else:
        r+=1
        l+=1
print(maxi)
        
        
            



