v = [5,7,4,8,2,6,1,3]
i = 0
tentativas = 0
while i< len(v):
    if i == 0 or v[i] >= v[i-1]:
        i += 1
    else:
        v[i], v[i-1] = v[i-1], v[i]
        i -= 1
        tentativas += 1
print(v, tentativas) 