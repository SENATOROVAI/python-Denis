my_str = '0409128473242875610432423'
a = list(my_str)
print(len(a))
for i in range(1, len(a)):
    for j in range(i, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
        else:
            break
print(*a)
