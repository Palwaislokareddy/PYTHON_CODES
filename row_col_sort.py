a=[[3,4,6,8],[5,7,9,10],[8,12,13,15],[20,23,26,28],[30,36,40,45]]
n=5
m=4
x=8
def binary(a, x, n, m):
    l = 0
    r = (n * m) - 1
    while l <= r:
        mid = (l + r) // 2
        row = mid // n
        col = mid % m
        if a[row][col] == x:
            return (row, col)
        elif a[row][col] > x:
            r = mid - 1
        else:
            l = mid + 1
    return None

res = binary(a, x, n, m)
if res:
    print(f"Found at position: {res}")
else:
    print("Not found")




            