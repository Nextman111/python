lst = [1, 3, 5, 6, 8]
max = lst[0]

for i in range(1, len(lst)):
    if lst[i] > max:
        max = lst[i]


print(f'Максимальное число {max}')