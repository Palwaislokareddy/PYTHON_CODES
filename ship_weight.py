#return the number of days to ship the weights
'''a=[1,2,3,4,5,6,7,8,9,10]
capacity=20
sums=0
count=1
for i in a:
    if i>capacity:
        print("not possible")
        break
    elif sums+i<=capacity:
        sums+=i
    else:
        count+=1
        sums=i
else:
    print(count)
'''    
#------------------------------------------or------------------------------------------------------------
w=[1,2,3,4,5,6,7,8,9,10]
capacity=12
d=1
s=0
if capacity<max(w):
    print('Not possible')
else:
    for i in w:
        if s+i<=capacity:
            s+=i
        else:
            d+=1
            s=i  

print(d)
print(d)

