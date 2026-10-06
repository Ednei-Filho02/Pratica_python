import random
random.seed(1279)
list = [3,4,1,2,5]
tentativas = 0

while list != sorted(list):
    random.shuffle(list)
    tentativas += 1

print(list, tentativas)