#task16
a = []
n = int(input('Введите размер массива: '))
print('Введите элементы массива: ')

for i in range(n):
    A = int(input())
    a.append(A)
x = int(input('Введите элемент для поиска X: '))
print(f'Кол-во вхождений x: {a.count(x)}')


#task18
a = []
n = int(input('Введите размер массива: '))
print('Введите элементы массива: ')

for i in range(n):
    A = int(input())
    a.append(A)
a = sorted(a)
x = int(input('Введите элемент для поиска X: '))
print('Ближайшее к заданному: ')

for j in range(n - 1):
    if a[j] <= x <= a[j + 1]:
        if abs(x - a[j]) <= abs(x - a[j + 1]):
            print(a[j])
        else:
            print(a[j + 1])
        break
    elif x < a[j]:
        print(a[j])
        break
    elif x > a[n - 1]:
        print(a[n - 1])
        break
   
#task20
s1 = 'AEIOULNSTRАВЕИНОРСТ'
s2 = 'DGДКЛМПУ'
s3 = 'BCMPБГЁЬЯ'
s4 = 'FHVWYЙЫ'
s5 = 'KЖЗХЦЧ'
s8 = 'JXШЭЮ'
s10 = 'QZФЩЪ'

word = input('Введите слово: ')
total = 0
word = word.upper()

for i in word:
    if i in s1:
        total += 1
    elif i in s2:
        total += 2
    elif i in s3:
        total += 3
    elif i in s4:
        total += 4
    elif i in s5:
        total += 5
    elif i in s8:
        total += 8
    elif i in s10:
        total += 10
print(total)
