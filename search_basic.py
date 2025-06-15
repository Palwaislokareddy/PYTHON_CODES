#search and print the max index of the element 
'''d=[2,4,3,1,4,2,3,4,5]
k=4
a=[]
for i in range(len(d)):
    if d[i]==k:
        a.append(i)
if a:
    print(max(a))
else:
    print("-1")
    '''
    
#-------------------------------or---------------------------
'''d=[2,4,3,1,4,2,3,4,5]
k=4
f=0
for i in range(len(d)):
    if d[i]==k:
        k=i
        f=1
if f==0:
    print(-1)
else:
    print(k)'''
#---------------------------------------------------------------
'''a=[2,3,3,5,6,7,7,8,9,10,10,10,13,15]
x=10
l=0
r=len(a)-1

while l<=r:
    mid=(l+r)//2
    if a[mid]==x:
        res=mid
        l=mid+1
        #h=mid-1  we will get the first occ
        break
    elif x<a[mid]:
        r=mid-1
    else:
        l=mid+1
if res!=-1:
    print(res)
else:
    print("not found")
    '''
#--------------------------------------------------------------------------------------------
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
    
        
    
    


    
