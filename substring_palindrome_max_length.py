#maximum length of the palindrome substring
'''s="ababba"
a=[]
maxi=0
for i in range(len(s)-1):
    for j in range(i+1,len(s)+1):
        a.append(s[i:j])
        
print(a)
for i in a:
    if i==i[::-1]:
        maxi=max(maxi,len(i))
print(maxi)'''

#-----------------------------------------------------------------------------------
'''a="ababba"
m=0
for i in range(len(a)):
    l=i
    r=i
    while l>=0 and r<len(a) and a[l]==a[r]:
        m=max(m,r-l+1)
        l=l-1
        r=r+1
    l=i
    r=i+1       
    while l>=0 and r<len(a) and a[l]==a[r]:
        m=max(m,r-l+1)
        l=l-1
        r=r+1
        
print(m)'''
#----------------------------------------------------------------
#printing longest palindrome and the count no of palindrome
a="ababba"
m=0
res=""
count=0
for i in range(len(a)):
    l=r=i
    while l>=0 and r<len(a) and a[l]==a[r]:
        count+=1
        if r-l+1>m:
            m=r-l+1
            res=a[l:r+1]         
        l=l-1
        r=r+1
    l=i
    r=i+1
    while l>=0 and r<len(a) and a[l]==a[r]:
        count+=1
        if r-l+1>m:
            m=r-l+1
            res=a[l:r+1]
        l=l-1
        r=r+1
    
print(m,res,count)
    
    
    

        

        
    
    
