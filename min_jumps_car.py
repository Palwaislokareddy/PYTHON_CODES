a=[2,1,4,3,5,1,2,4,2,1,1,2,0]
'''m=0
c=0
end=0
for i in range(len(a)-1):
    if i+a[i]>m:
        m=i+a[i]
    if i==end:
        c+=1
        end=m
print(c)'''

#or-----------------------------------------------------------------------------------------
l=0
r=0
jump=0
while r<len(a)-1:
    m=0
    for i in range(l,r+1):
        if i+a[i]>m:
            m=i+a[i]
    l=r+1
    r=m
    jump+=1
print(jump)
    
    