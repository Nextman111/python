#5 10 15 но не 30
num = int(input('num = '))
print((num % 5 == 0
      and num % 10 == 0
      or num % 15 == 0)
      and num % 30 != 0)