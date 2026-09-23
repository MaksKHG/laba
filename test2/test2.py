value = int(input('Введите расстояние: '))
unit_from = input(
    'Из какой единицы переводим '
    '(км, м, см, мм, mi, yd): '
).lower()
unit_to = input(
    'В какую единицу переводим '
    '(км, м, см, мм, mi, yd): '
).lower()

units = {
    'км': 1000,
    'м': 1,
    'см': 0.01,
    'мм': 0.001,
    'mi': 1609.344,
    'yd': 0.9144,
}

if unit_from in units and unit_to in units:
    value_in_meters = value * units[unit_from]
    result = value_in_meters / units[unit_to]
    print(f'{value} {unit_from} = {result:.4f} {unit_to}')
else:
    print('Ошибка: указана неизвестная единица измерения')
