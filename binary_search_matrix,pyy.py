'''a=[[1,2,3],[4,5,6],[7,8,9]]
d=5
flag=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i][j]==d:
            print("found",[i,j])
            flag=1
            break
    
    if flag==1:
        break
else:
    print("not found")'''
#---------------------------------------------------------------------------------

'''a=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
x=26
found=False
def binary(a,x):
    l=0
    r=len(a)-1
    while l<=r:
        mid=(l+r)//2
        if a[mid]==x:
            return mid
        elif a[mid]>x:
            r=mid-1
        else:
            l=mid+1
    return -1
        
for i in range(len(a)):
    
    if a[i][0]<=x <= a[i][-1]>=x:
        j=binary(a[i],x)
        if j != -1:
            print(f"Found at row {i}, column {j}")
            found = True
            break
if not found:
    print("Not found")'''
#-------------------------------------------------------------

'''def binary(a,x,n,m):
    l=0
    r=(n*m)-1
    while l<=r:
        mid=(l+r)//2
        if a[mid//4][mid%4]==x:
            return 1
        elif a[mid//4][mid%4]>x:
            r=mid-1
        elif a[mid//4][mid%4]<x:
            l=mid+1
    return 0
a=[[2,3,7,8],[9,15,20,22],[23,26,35,37],[38,39,42,43]]
n=4
m=4
x=8
if binary(a,x,n,m):
    print("found")
else:
    print("not found")'''
#-------------------------------------------------------------------------
#Finding the element in the matrix using order and binary method(74)
def binary(a,x,n,m):
    l=0
    r=(n*m)-1
    while l<=r:
        mid=(l+r)//2
        if a[mid//m][mid%m]==x:
            return 1
        elif a[mid//m][mid%m]>x:
            r=mid-1
        elif a[mid//m][mid%m]<x:
            l=mid+1
    return 0
a=[[2,3,7,8],[9,15,20,22],[23,26,35,37]]
n=3
m=4
x=8
if binary(a,x,n,m):
    print("found")
else:
    print("not found")



            