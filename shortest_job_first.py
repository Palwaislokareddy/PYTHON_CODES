a=[4,3,7,1,6,2]
a.sort()
sums=0
b=0
for i in range(0,len(a)-1):
    b+=a[i]
    sums+=b
avg=sums/len(a)
print(avg)

    