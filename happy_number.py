def happy_number(n):
        if n<1:
            return False
        if n==1:
            return True
        else:
            a=set()
            while n!=1:
                total=0
                for d in str(n):
                    total+=int(d)**2   
                if total in a:
                    return False
                a.add(total)
                n=total
            return True
n=int(input())
print(happynumber(n))
            