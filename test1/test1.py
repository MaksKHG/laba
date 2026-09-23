import math

a = int(input('Введите сторону треугольника a:'))
b = int(input('Введите сторону треугольника b:'))
c = int(input('Введите сторону треугольника c:'))

if a + b > c and b + c > a and c + a > b:
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f'Площадь треугольника: {s:.2f}')
else:
    print('Треугольник не существует')
