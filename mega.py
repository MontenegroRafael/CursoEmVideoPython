import random

n1 = random.randint(1, 60)
n2 = random.randint(1, 60)
n3 = random.randint(1, 60)
n4 = random.randint(1, 60)
n5 = random.randint(1, 60)
n6 = random.randint(1, 60)
if n1 == n2:
    while n1 == n2:
        n2 = random.randint(1, 60)
elif n1 == n3:
    while n1 == n3:
        n3 = random.randint(1, 60)
elif n1 == n4:
    while n1 == n4:
        n4 = random.randint(1, 60)
elif n1 == n5:
    while n1 == n5:
        n5 = random.randint(1, 60)
elif n1 == n6:
    while n1 == n6:
        n6 = random.randint(1, 60)

elif n2 == n3:
    while n2 == n3:
        n3 = random.randint(1, 60)
elif n2 == n4:
    while n2 == n4:
        n4 = random.randint(1, 60)
elif n2 == n5:
    while n2 == n5:
        n5 = random.randint(1, 60)
elif n2 == n6:
    while n2 == n6:
        n6 = random.randint(1, 60)

elif n3 == n4:
    while n3 == n4:
        n4 = random.randint(1, 60)
elif n3 == n5:
    while n3 == n5:
        n5 = random.randint(1, 60)
elif n3 == n6:
    while n3 == n6:
        n6 = random.randint(1, 60)

elif n4 == n5:
    while n4 == n5:
        n5 = random.randint(1, 60)
elif n4 == n6:
    while n4 == n6:
        n6 = random.randint(1, 60)

elif n5 == n6:
    while n5 == n6:
        n6 = random.randint(1, 60)


print(' {} - {} - {} - {} - {} - {} '.format(n1, n2, n3, n4, n5, n6))
