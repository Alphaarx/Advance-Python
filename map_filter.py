l=[1,2,3,4,5]
square=lambda x: x*x

#MAP    map(function, iterable)
newl=map(square,l)
print(list(newl))
#FILTER filter(function, iterable)
def is_even(x):
    return x%2==0
newl=filter(is_even,l)
print(list(newl))
#Reduce reduce(function, iterable)
from functools import reduce
sum=lambda x,y: x+y
newl=reduce(sum,l)
print(newl)
