##sorting two sorted list
n=[2,4,5,8,9,20]
m=[3,5,6,9,11,12,13,30]
'''a=n+m
for j in range(len(a)-1):
f=False
    for i in range(len(a)-1-j):
        if(a[i]>a[i+1]):
            f=True
            a[i],a[i+1]=a[i+1],a[i]
    if f==False:
        break
print(a)'''
#----------------------------------------------------------------------or-----------------------------------------------------------
l=[]
i=j=0
while i<len(n) and j<len(m):
    if n[i]<m[j]:
        l.append(n[i])
        i+=1
    else:
        l.append(m[j])
        j+=1
l.extend(n[i:])
'''while j<len(b):
    l.append(b[j])
    j+=1
while i<len(a):
    l.append(a[i]) ##extend line can replace by this code
    i+=1'''
l.extend(m[j:])
print(l)

#--------------------------------------------------------------or---------------------------------------------------------------

'''l1=[2,4,5,8,9]
l2=[3,5,6,9,11,12,13]
i=0
j=0
a=[]
for _ in range(len(l1) + len(l2)):
    if i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            a.append(l1[i])
            i += 1
        else:
            a.append(l2[j])
            j += 1
    elif i >= len(l1) and j < len(l2):
        a.append(l2[j])
        j += 1
    elif j >= len(l2) and i < len(l1):
        a.append(l1[i])
        i += 1

print(a)'''

