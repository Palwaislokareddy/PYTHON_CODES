a=[0,3,8,1,5,7,9]
b=[5,7,10,2,6,9,11]
jobs=list(zip(a,b))
jobs.sort(key=lambda x:x[1])
'''def fun(jobs):
    return x[1]'''# lambda function
print(jobs)
last=0
count=0
for i in jobs:
    if i[0]>last:
        count+=1
        last=i[1]
print(count)
        
 
    
        