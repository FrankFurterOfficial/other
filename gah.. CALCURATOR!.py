a = int(input('hi '))
b = int(input('hi '))
c = input('huh  ')
import random as r

#------------------------------------------------------------
# #50% chance to not work
# z = r.randint(0,1)
# if z == 1:
#     if c == 'multiply':
#         print('1')
#         print(a, 'x', b, '=', a*b)
#     elif c == 'add':
#         print('2')
#         print(a, '+', b, '=', a+b)
#     elif c == 'subtract':
#         print('3')
#         print(a, '-', b, '=', a-b)
#     elif c == 'divide':
#         print('4')
#         print(a, '/', b, '=', a/b)
#     else:
#         print('erm try again buddy')
# else:
#     print(z)
#     print('better luck next time')

#------------------------------------------------------------
#50% chance to just flat out lie
z = r.randint(0,1)

if c == 'multiply':
    print('1')
    if z == 0:
        print(a, 'x', b, '=', a*b)
    elif z == 1:
        #print('LYING')
        print(a, 'x', b, '=', r.randint((a*b)-10,(a*b)+10))
elif c == 'add':
    print('2')
    if z == 0:
        print(a, '+', b, '=', a+b)
    elif z == 1:
        #print('LYING')
        print(a, 'x', b, '=', r.randint((a+b)-10,(a+b)+10))
elif c == 'subtract':
    print('3')
    if z == 0:
        print(a, '-', b, '=', a-b)
    elif z == 1:
        #print('LYING')
        print(a, '-', b, '=', r.randint((a-b)-10,(a-b)+10))
elif c == 'divide':
    print('4')
    if z == 0:
        print(a, '/', b, '=', a/b)
    elif z == 1:
        #print('LYING')
        print(a, '/', b, '=', r.randint((a/b)-10,(a/b)+10))
else:
    print('erm try again buddy')