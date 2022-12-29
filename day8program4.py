def div(a,b):
    assert( isinstance(a,int)or isinstance(a,float)), "first argument should be either integer or float"
    assert( isinstance(b,int)or isinstance(b,float)), "second argument should be either integer or float"
    assert(b!=0),"division by zero is not defined"
    return a/b
try:
    print(div(55,0))
except Exception as obj:
    print(obj)
try:
    print(div(20,3))
except Exception as obj:
    print(obj)

try:
    print(div(100,"hello"))
except Exception as obj:
    print(obj)
try:
    print(div("hello",20))
except Exception as obj:
    print(obj)
    
