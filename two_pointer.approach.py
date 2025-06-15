a=[2,7,11,15]
x=9
i=0
j=len(a)-1
while i<j:
    if a[i]+a[j]==x:
        print(i,j)
        break
    elif a[i]+a[j]>x:
        j-=1
    else:
        i+=1

            