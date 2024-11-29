# Математические формулы
4 программы, в каждой из которой находятся функции по вычислению периметра и площади для конкретной фигуры(круг, квадрат, треугольник, прямоугольник)
## Круг [`circle.py`](../circle.py)
- `area(r)` - находит площадь по заданному значению радиуса r
- `perimeter(r)` - находит периметр по заданному значению радиуса r

## Прямоугольник [`rectangle.py`](../rectangle.py)
- `area(a, b)` - находит площадь по заданным значениям длины и ширины прямоугольника a и b соответственно
- `perimeter(a, b)` - находит периметр по аналогичным параметрам a и b

## Квадрат [`square.py`](../square.py)
- `area(a)` - находит площадь по заданному значению стороны квадрата a
- `perimeter(a)` - находит периметр по заданному значению стороны квадрата a

## Треугольник [`triangle.py`](../triangle.py)
- `area(a, h)` - находит площадь по заданным значению стороны и высоты треугольника, проведенной к ней, a и h соответсвенно
- `perimeter(a, b, с)` - находит периметр по переданным значениям сторон треугольника a, b, c

## Пример вызова
Для `circle.py`:
```
r = int(input("Введите радиус круга"))
a = area(r) # Вызываем функцию area с аргументом r
p = perimeter(r) # Вызываем функцию perimeter с аргументом r
print("Площадь круга:", a)
print("Периметр круга:", p)
```

Для `triangle.py`:
```
a = int(input("Введите основание треугольника"))
b = int(input("Введите вторую сторону треугольника"))
c = int(input("Введите третью сторону треугольника"))
h = int(input("Введите высоту треугольника"))
ar = area(a, h) # Вызываем функцию area с аргументом a, h
per = perimeter(a, b, c) # Вызываем функцию perimeter с аргументами a, b, c
print("Площадь треугольника:", ar)
print("Периметр треугольника:", per)
```

Для `rectangle.py`:
```
a = int(input("Введите длину прямоугольнкиа"))
b = int(input("Введите ширину прямоугольника"))
ar = area(a, b) # Вызываем функцию area с аргументом a, b
per = perimeter(a, b) # Вызываем функцию perimeter с аргументами a, b
print("Площадь прямоугольника:", ar)
print("Периметр прямоугольника:", per)
```

Для `square.py`:
```
a = int(input("Введите сторону квадрата"))
ar = area(a) # Вызываем функцию area с аргументом a
per = perimeter(a) # Вызываем функцию perimeter с аргументами a
print("Площадь квадрата:", ar)
print("Периметр квадрата:", per)
```


## Тесты
Для проверки корректной работоспособности каждого файлы были добавлены следующие тесты:
- [`test_circle.py`](https://github.com/kavalski316/geometric_lib/blob/new_features_465315/tests/test_circle.py) -  для проверки 'circle.py'
- [`test_rectangle.py`](https://github.com/kavalski316/geometric_lib/blob/new_features_465315/tests/test_rectangle.py) -  для проверки 'rectangle.py'
- [`test_square.py`](https://github.com/kavalski316/geometric_lib/blob/new_features_465315/tests/test_square.py) -  для проверки 'square.py'
- [`test_triangle.py`](https://github.com/kavalski316/geometric_lib/blob/new_features_465315/tests/test_triangle.py) -  для проверки 'triangle.py'

# История изменений
1. `8ba9ae` - добавлены файлы `circle.py` и `square.py`
2. `d078c8` - добавлены документы
3. `2ee72e` - добавлен файл `rectangle.py`
4. `f24a9c` - исправлена ошибка в файле `rectangle.py` и добавлен `triangle.py`
5. `68cbec` - добавлена документация в файлах `circle.py`, `rectangle.py`, `square.py`, `triangle.py`
6. `32677a` - добавлены тесты