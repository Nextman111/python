n = int(input('N = '))
nums = []
for i in range (-abs(n), abs(n)+1):
    nums.append(i)
print(nums)

for i in range (-abs(n), abs(n)+1):
    print(i, end = ' ')
