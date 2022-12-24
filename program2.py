Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
lst1=list()
type(lst1)
<class 'list'>
lst1.append(10)
lst1
[10]
lst1.append(15)
lst1.append(10)
lst1
[10, 15, 10]
lst1.append('python')
lst1
[10, 15, 10, 'python']
lst1.clear()
lst1
[]
lst1=[10,15,15,10,python]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    lst1=[10,15,15,10,python]
NameError: name 'python' is not defined
lst1=[10,15,15,10,'python']
lst1.count(10)
2
lst1.append('mca')
lst1
[10, 15, 15, 10, 'python', 'mca']
lst1.count('python')
1
lst1.count(10)
2
lst1.count(15)
2
lst1.count('mass')
0
len(lst1)
6
lst2=lst1
lst1
[10, 15, 15, 10, 'python', 'mca']
lst2
[10, 15, 15, 10, 'python', 'mca']
del lst2[-1]
lst2
[10, 15, 15, 10, 'python']
lst1
[10, 15, 15, 10, 'python']
lst3=lst1.copy()
print(id(lst1),id(lst3))
2574533446784 2574533311040
lst1
[10, 15, 15, 10, 'python']
lst3
[10, 15, 15, 10, 'python']
lst3.append(240)
lst3.append(142)
lst3
[10, 15, 15, 10, 'python', 240, 142]
lst1
[10, 15, 15, 10, 'python']
lst2=lst1.copy()
lst1
[10, 15, 15, 10, 'python']
lst4=lst1[:]
print(id(lst1),(lst4))
2574533446784 [10, 15, 15, 10, 'python']
print(id(lst1),(lst4))
2574533446784 [10, 15, 15, 10, 'python']
print(id(lst1),id(lst4))
2574533446784 2574537687808
lst1
[10, 15, 15, 10, 'python']
lst1[:]
[10, 15, 15, 10, 'python']
lst1[1:]
[15, 15, 10, 'python']
lst1.append([11,22])
lst1
[10, 15, 15, 10, 'python', [11, 22]]
lst1[-1]
[11, 22]
lst1[1]
15
lst1.append[('c','java','python','c++')]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    lst1.append[('c','java','python','c++')]
TypeError: 'builtin_function_or_method' object is not subscriptable
lst1.append('c','java','c++')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    lst1.append('c','java','c++')
TypeError: list.append() takes exactly one argument (3 given)
lst1.append(('c','c++','java'))
\
lst1
[10, 15, 15, 10, 'python', [11, 22], ('c', 'c++', 'java')]
lst1.append('hello')
lst1
[10, 15, 15, 10, 'python', [11, 22], ('c', 'c++', 'java'), 'hello']
lst2
[10, 15, 15, 10, 'python']
lst1.count(11)
0
lst1.count('hello')
1
del lst1[3:5]
lst1
[10, 15, 15, [11, 22], ('c', 'c++', 'java'), 'hello']
lst1.extend([23,26])
lst1
[10, 15, 15, [11, 22], ('c', 'c++', 'java'), 'hello', 23, 26]
lst1.extend(['uma','raviteja','donseenu'])
lst1
[10, 15, 15, [11, 22], ('c', 'c++', 'java'), 'hello', 23, 26, 'uma', 'raviteja', 'donseenu']
lst1.index('uma')
8
lst1.index('hello')
5
lst1.insert(0,'lokesh kanagaraj')
lst1
['lokesh kanagaraj', 10, 15, 15, [11, 22], ('c', 'c++', 'java'), 'hello', 23, 26, 'uma', 'raviteja', 'donseenu']
lst1.del(4)
SyntaxError: invalid syntax
del lst1[4]
lst1
['lokesh kanagaraj', 10, 15, 15, ('c', 'c++', 'java'), 'hello', 23, 26, 'uma', 'raviteja', 'donseenu']
lst1.insert(5,'massmaharaja')
lst1
['lokesh kanagaraj', 10, 15, 15, ('c', 'c++', 'java'), 'massmaharaja', 'hello', 23, 26, 'uma', 'raviteja', 'donseenu']
lst1.index('massmaharaja')
5
lst1.index(c,2)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    lst1.index(c,2)
NameError: name 'c' is not defined
lst1.index('c',2)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    lst1.index('c',2)
ValueError: 'c' is not in list
lst1.index('uma',2)
9
lst1
['lokesh kanagaraj', 10, 15, 15, ('c', 'c++', 'java'), 'massmaharaja', 'hello', 23, 26, 'uma', 'raviteja', 'donseenu']
lst1.pop()
'donseenu'
lst1
['lokesh kanagaraj', 10, 15, 15, ('c', 'c++', 'java'), 'massmaharaja', 'hello', 23, 26, 'uma', 'raviteja']
a=lst1.pop()
a
'raviteja'
lst1
['lokesh kanagaraj', 10, 15, 15, ('c', 'c++', 'java'), 'massmaharaja', 'hello', 23, 26, 'uma']
a=list1.pop(4)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a=list1.pop(4)
NameError: name 'list1' is not defined. Did you mean: 'lst1'?
a=list1.pop(4)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a=list1.pop(4)
NameError: name 'list1' is not defined. Did you mean: 'lst1'?
a=list1.pop(3)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a=list1.pop(3)
NameError: name 'list1' is not defined. Did you mean: 'lst1'?
a=lst1.pop(4)
lst1
['lokesh kanagaraj', 10, 15, 15, 'massmaharaja', 'hello', 23, 26, 'uma']
b=[]
b
[]
b.pop()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    b.pop()
IndexError: pop from empty list
lst1
['lokesh kanagaraj', 10, 15, 15, 'massmaharaja', 'hello', 23, 26, 'uma']
lst1.remove(15)
lst1
['lokesh kanagaraj', 10, 15, 'massmaharaja', 'hello', 23, 26, 'uma']
lst1.reverse()
lst1
['uma', 26, 23, 'hello', 'massmaharaja', 15, 10, 'lokesh kanagaraj']
L1=[3,84,45,2354,545,98,34,27]
L2=['uma','harish','guru','diwakar','ashok']
L1
[3, 84, 45, 2354, 545, 98, 34, 27]
L1.sort[]
SyntaxError: invalid syntax
L1.sort()
L1
[3, 27, 34, 45, 84, 98, 545, 2354]
L2.sort()
L2
['ashok', 'diwakar', 'guru', 'harish', 'uma']
L1.sort(reverse=True)
L1
[2354, 545, 98, 84, 45, 34, 27, 3]
L2.sort(reverse=True)
L2
['uma', 'harish', 'guru', 'diwakar', 'ashok']
