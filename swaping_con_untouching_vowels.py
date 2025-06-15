
#swaping the conso and untoching the vowels 
s="hippopotamus"
d='aeiou'
a=list(s)
l=0
r=len(a)-1
while l<r:
    if a[l] in d:
        l+=1
    elif a[r] in d:
        r-=1
    else:
        a[l],a[r]=a[r],a[l]
        l+=1
        r-=1
print("".join(a))
        
        