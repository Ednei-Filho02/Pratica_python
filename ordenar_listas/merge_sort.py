v = [ 7, 4, 2, 1, 8, 3, 6, 5 ]

def merge_sort(v):
    if len(v) <=1:
        return v 
    m = len(v)//2
    a = merge_sort(v[:m])
    b = merge_sort(v[m:])
    r = []

    while a and b:
        if a[0] <= b[0]:
            r.append(a.pop(0))
        else:
            r.append(b.pop(0))
    return r + a + b

print(merge_sort(v))
        
    