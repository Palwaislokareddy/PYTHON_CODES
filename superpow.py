def superPow(a,b):
        mod=1337
        res=1
        for d in b:
            res=pow(res,10,mod)*pow(a,d,mod)%mod
        return res
print(superPow(a,b))