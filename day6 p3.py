Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
coord=(3,5)
abc=(2,9)
type(coord)
<class 'tuple'>
type(abc)
<class 'tuple'>
abc[0]
2
print('x:(0[0]); y: ([1]);abc : (1[0]),1[1])'.format(coord,abc))
x:(0[0]); y: ([1]);abc : (1[0]),1[1])
print('x:{0[0]}; y:{0[1]};abc : {1[0]},{1[1])}'.format(coord,abc))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print('x:{0[0]}; y:{0[1]};abc : {1[0]},{1[1])}'.format(coord,abc))
ValueError: Only '.' or '[' may follow ']' in format field specifier

print('x:{0[0]}; y:{0[1]};abc : {1[0]},{1[1])}'.format(coord,abc))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print('x:{0[0]}; y:{0[1]};abc : {1[0]},{1[1])}'.format(coord,abc))
ValueError: Only '.' or '[' may follow ']' in format field specifier
print('x:{0[0]}; y:{0[1]};abc : {1[0]},{1[1]}'.format(coord,abc))
x:3; y:5;abc : 2,9
