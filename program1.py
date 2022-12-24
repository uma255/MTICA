Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'hello'"world"'python'
'helloworldpython'
a='hello'"world"'python'
a
'helloworldpython'
a="hello","world",'python'
a
('hello', 'world', 'python')
type(a)
<class 'tuple'>
a=23,7.9,'python',5+8j,'c'
a
(23, 7.9, 'python', (5+8j), 'c')
a=(5)
b=(5.8)
c=('hello')
type(a)
<class 'int'>
a(5,)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a(5,)
TypeError: 'int' object is not callable
a=(5,)
a
(5,)
a=(6,)
type(a)
<class 'tuple'>
