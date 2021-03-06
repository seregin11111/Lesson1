"""Задание
1) Взять код, подготовленный ранее
2) Провести его ревизию на соответствие PEP 8
3) Сравнить было-стало
4) Объяснить что стало лучше или хуже с т.з. читаемости кода и почему.
"""

"""Код из задания #2 Lesson2.py
197 проблем из Pysharm

1. Комменты должны начинаться с "# "
Улучшилась читаемость

2. Много скрытых строк, начинающихся с #
Заменил на кавычки тройные

2. Встроенное имя list
Переименовал, чтобы не использовать встроенные названия

3. При перечислении списка выровнял строки по вертикали.
Улучшилась читаемость"""

""" Описать некоторую предметную область (не выбор) словарем, списком и множеством (-ами).
    Оценить удобство каждого из способов.
    Реализовать поиск элемента.

    Список: 1. Упорядочен 2. Не обязательно хэшируемые элементы
    Множество:  1. Неупорядочно 2. Хэшируемые элементы 3. Уникальные элементы.
    Словарь: 1. Неупородячен 2. Не допускает повторы, ключи уникальны."""


def a_list():
    sklad_list = ['Кранбукса', 'Смеситель для душа', 'Лейка душевая',
                  'Смеситель для кухни', 'Cмеситель для раковины',
                  'Стойка душевая', 'Подводка гибкая', 'Шланг для душа',
                  'Смеситель для кухни настенный', 'Стойка']
    x = input('Ввести наименование товара со склада сантехники ')
    if x.title() in sklad_list:
        print('Товар данного наименования есть на складе')
    else:
        print('Данного товара на складе нет')
    nomer = int(input('Введите номер из списка товаров'))
    if sklad_list[nomer]:
        print('Наименование:', sklad_list[nomer])
    else:
        print('Данного товара на складе нет')


def a_set():
    sklad_set = {'Кранбукса', 'Смеситель для душа', 'Лейка душевая',
                 'Смеситель для кухни', 'Cмеситель для раковины',
                 'Стойка душевая', 'Подводка гибкая', 'Шланг для душа',
                 'Смеситель для кухни настенный', 'Стойка'}
    x = input('Ввести наименование товара со склада сантехники ')
    if x.title() in sklad_set:
        print('Товар данного наименования есть на складе')
    else:
        print('Данного товара на складе нет')


def a_dict():
    sklad_dict = {'Кранбукса': 'Запасные части',
                  'Смеситель для душа': 'Смесителя',
                  'Смеситель для кухни': 'Смесителя',
                  'Смеситель для раковины': 'Смесителя',
                  'Лейка душевая': 'Запасные части',
                  'Стойка душевая': 'Запасные части',
                  'Шланг для душа': 'Запасные части',
                  'Смеситель для кухни настенный': 'Смесителя',
                  'Подводка гибкая': 'Запасные части'}
    x = input('Ввести наименование товара со склада сантехники ')
    if x.title() in sklad_dict:
        print('Товар данного наименования есть на складе. Товар в разделе:', sklad_dict[x])
    else:
        print('Данного товара на складе нет')


def m():
    print(''' Производим поиск в:
                1 - Список
                2 - Множество
                3 - Словарь
                4 - Выход ''')
    choise = int(input('Введите выбор: '))
    if choise == 1:
        a_list()
    elif choise == 2:
        a_set()
    elif choise == 3:
        a_dict()
    elif choise == 4:
        print('Выход')
    else:
        print('Такого пункта нет')


m()