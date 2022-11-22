a = 7.893

print(int((a%1) * 10))

b = '7.893'
for i in range(len(b)):
    if b[i] == '.':
        print(b[i+1])
        break
