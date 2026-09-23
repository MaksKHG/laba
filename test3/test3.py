god = int(input('Введите год'))

if god % 400 == 0 or (god % 4 == 0 and god % 100 != 0):
    print('Год високосный')
else:
    print('Год не високосный')
