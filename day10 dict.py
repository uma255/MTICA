Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dict1={'Name':'vikram','Age':'7','Class':'first'}
print(dict1)
{'Name': 'vikram', 'Age': '7', 'Class': 'first'}
print(dict1['Name'])
vikram
print(dict1['Age'])
7
print(dict1['class'])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(dict1['class'])
KeyError: 'class'
print(dict1['Class'])
first
print(dict1)
{'Name': 'vikram', 'Age': '7', 'Class': 'first'}
dict1['Age']=8
print(dict1)
{'Name': 'vikram', 'Age': 8, 'Class': 'first'}
dict1['Course']=MCA
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dict1['Course']=MCA
NameError: name 'MCA' is not defined
NameError: name 'MCA' is not defined
SyntaxError: invalid syntax
dict1['Course']='MCA'
print(dict1)
{'Name': 'vikram', 'Age': 8, 'Class': 'first', 'Course': 'MCA'}
del dict1['Class']
print(dict1)
{'Name': 'vikram', 'Age': 8, 'Course': 'MCA'}
dict1.clear()
print(dict1)
{}
dict1={'Name':'vikram','Age':'7','Class':'first'}
print(dict1)
{'Name': 'vikram', 'Age': '7', 'Class': 'first'}
del dict1
print(dict1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(dict1)
NameError: name 'dict1' is not defined. Did you mean: 'dict'?
dict1.keys
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    dict1.keys
NameError: name 'dict1' is not defined. Did you mean: 'dict'?
dict1={'Name':'vikram','Age':'7','Class':'first'}
dict1.keys()
dict_keys(['Name', 'Age', 'Class'])
dict1.values()
dict_values(['vikram', '7', 'first'])
dict1.items()
dict_items([('Name', 'vikram'), ('Age', '7'), ('Class', 'first')])
for i in dict1:print(i)

Name
Age
Class
for i in dict1:keys():print(i)
SyntaxError: illegal target for annotation
for i in dict1.keys():print(i)

Name
Age
Class
for i,j in dict1.items():print(i,j)

Name vikram
Age 7
Class first
