def kelvintofahrenheit(temperature):
    assert(temperature>=0),"colder than absolute zero at mqhuhh"
    res=((temperature-273)*1.8)+32
    return res

try:
    print(kelvintofahrenheit(-50))
except Exception as ab:
    print(ab)
try:
    print(kelvintofahrenheit(273))
except Exception as ab:
    print(ab)
try:
    print(kelvintofahrenheit(505.78))
except Exception as ab:
    print(ab)
try:
    print(kelvintofahrenheit(-5))
except Exception as ab:
    print(ab)
print("thank you")
