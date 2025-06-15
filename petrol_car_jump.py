a=[2,2,1,0,1,3,0]
s=0
for i in range(1,len(a)):
    if s<0:
        print("np")
        break
    s=max(s,a[i])
    s-=1
else:
    print("possible")
   
        
        