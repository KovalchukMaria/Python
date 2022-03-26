a = int (input('введите любое целое число'))
while a // 10 > 1:
    b = a % 10
    c = a // 10
    d = c % 10
    a = a // 10
if b < d:
   b = d
if b >= d:
    b = b
print ('самая большая цифра в числе - это ' ,b)
     
