"""
Коментарии
Коментарии
Коментарии
"""
#что такое переменная?


is_student = True

name = input('введите имя:')

print('hello, ' ,name, '!')

#что такое тип данных
#скалярные типы данных хранит только одно значение

# bool - два допустимых значения True, False
# int - целочисленные
i1 = 666
i2 = 0x59 # шестнадцатиричная СС
i3 = 0b101010 # двоичная система СС
i4 = 0o255 # восьмиричная CC

# float - с плавающей точкой
f1 = 1.23
f2 = 12e-3 # 12 * 10 ^-3
f3 = 12e3 # 12* 10^3

# str - строковый
# bytes = байтовая строка
s1 = 'Some string'
s2 = "Some string"
s3 = r'Raw string' # сырые строки
s4 = u'Hello' #u юникод это на 2
s5 = b'na russkom pisat tut nelza' # это строка просто байтовая типа там что угодно
s6 = ''' это будет воспринято не
 как коментарий а как строка перенос строки 
 там и все такое'''
print(s6)
#\ при помощи палки экранирую

# Комплексные числа - complex
с1 = 3.14j

# Cтруктурированные (сложные) может хранит любые типы и много значений всяких разных
# tuple, list, set, dict, object

#кортежи - tuple это () скобки
t1 = (1,) # кортеж из одного элемента ВСЕГДА СТАВИТЬ ЗАПЯТУЮ
t2 = (True, 6, 1.2, 'String', (1,2,3))

# списки - list
lst1 = [[1],[2],3,False,(2,3,4)]

#множества - set множество выводит только различные элементы
#

s1 = {1,2,3}
s2 = set() # пустое множество
s3 = set([1,2,3]) # это тоже самое что s1

print(s2)
print(t2[1], lst1[2], lst1[0][0])

#словари - dict всегда список в низ писать

d = {
    'id': 1,
    'name': 'Саша'
    'is_student' : True,
    'skills': ('python', 'linux')
    }

#специальные типы
#None - пустота

a = None






