def merge_sort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    left=merge_sort(a[:mid])
    right=merge_sort(a[mid:])
    return merge(left,right)
def merge(left,right):
    l=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    while j<len(right):
        l.append(right[j])
        j+=1
    while i<len(left):
        l.append(left[i]) ##extend line can replace by this code
        i+=1
    return l
a=[11,3,5,7,8,11,1,12]
print(merge_sort(a))
