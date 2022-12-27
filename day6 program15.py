Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('{0},{1},{0},{0},{3},{2}'.format('apple','bannana','carrot','pen'))
apple,bannana,apple,apple,pen,carrot
print('{0},{1},{0}{0}{3},{2}'.format('apple','bannana','carrot','pen'))
apple,bannana,appleapplepen,carrot
print('{0},{1}{0}{0}{3}{2}'.format('apple','bannana','carrot','pen'))
apple,bannanaappleapplepencarrot
print('{0} {1} {0} {0} {3} {2}'.format('apple','bannana','carrot','pen'))
apple bannana apple apple pen carrot
print('lokesh purchased a kg of {},a dozen of {} and half kg of {}'.format('apple','bannana','carrot'))
lokesh purchased a kg of apple,a dozen of bannana and half kg of carrot
print('lokesh purchased a kg of {},a dozen of {} and half kg of {}'.format('apple','bannana','carrot'))
lokesh purchased a kg of apple,a dozen of bannana and half kg of carrot
print('lokesh kanagaraj first telugu movie is {} and second film is {} finally last film is {}'.format('kaithi','master','vikram'))
lokesh kanagaraj first telugu movie is kaithi and second film is master finally last film is vikram
print('kaithi movie is directed by {} and {} is also directed by him').format('lokesh kanagaraj','vikram')
kaithi movie is directed by {} and {} is also directed by him
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print('kaithi movie is directed by {} and {} is also directed by him').format('lokesh kanagaraj','vikram')
AttributeError: 'NoneType' object has no attribute 'format'
print('kaithi movie is directed by {}, and {}, is also directed by him').format('lokesh kanagaraj','vikram')
kaithi movie is directed by {}, and {}, is also directed by him
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print('kaithi movie is directed by {}, and {}, is also directed by him').format('lokesh kanagaraj','vikram')
AttributeError: 'NoneType' object has no attribute 'format'
