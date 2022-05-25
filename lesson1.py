1)
n = 88888888
i = 1  
s = 0  
while i <= n:  # включая n
    s = i + s 
    i = i + 1 
print ('Сумма ряда от 0 до', n, '=', s)

2)
n = [3, 4, 56, 100, 2, 2, 3]
i = 0 #счетчик
k = 0 #счетчик элементов в списке
sum = 0 #сумма элементов в списке
while i < len(n):
    sum = sum + n[i]
    i = i + 1 
    k = k + 1 
sred = sum / k #вычисляем среднее арифметическое
print ("Среднее арифметическое ряда = ", sred)

3)#Заменить в строке "asdxfghyxyx" все буквы "х" на "у"
stroka = 'asdxfghyxyx'
symbol_x = 'x'
symbol_y = 'y'
s = ''
for symbol_stroka in stroka:
    if symbol_stroka == symbol_x: 
        s+= symbol_y
    else:
        s+= symbol_stroka

print ('Получилась строка: ',s)

4)#4) Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30], кратных и 3 и 5.
s = [3, 4, 56, 100, 15, 2, 20, 30]
itog = 1
i = 0
while i < len(s):
    if s[i]/3 - int(s[i]/3) == 0:
        if s[i]/5- int(s[i]/5) == 0:
            itog= itog* s[i]
    i = i + 1 
print ('Итого= ',itog)

5)#Заменить в строке "asdxfghyxyx" все буквы "х" на "у"
stroka = 'asdxfghyxyx'
stroka = stroka.replace('x','y')
print ('Получилась строка: ',stroka)
