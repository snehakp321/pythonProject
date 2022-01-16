# please refer the below link for more info-
# https://www.geeksforgeeks.org/args-kwargs-python/
def myfunc(a, b):
    # Returns 5% of sum a and b
    return ((a + b) * 0.05)


result = myfunc(2, 3)
print(result)

print("--------------------------------------------------")
# where a and b are positional arguments and it is mixed
# when the parameter are not fixed and it can take arbitary number of arguments, star args comes into picture
# args are used by convention but any random keyword can be used
# args return tuples whereas kwargs return dictionary

def myfunc1(*args):
    return sum(args) * 0.05


result1 = myfunc1(1, 2, 3, 4, 5, 6, 7, 89, 90)
print(result1)

print("--------------------------------------------------")

def myfunc2(*args):
    for item in args:
        print(item)

myfunc2(1, 2, 3, 4, 5, 6, 7, 89, 90)

print("--------------------------------------------------")

# kwargs - dictionary

def myfunc2(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('my favorite fruit is {}'.format(kwargs['fruit']))
    else:
        print("I don't like anything! Bye")


myfunc2(fruit='mango',car='benz')

print("--------------------------------------------------")

def myfunc3(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['fruit']))

myfunc3(1,2,3,4,fruit='apple',car='benz')

print("--------------------------------------------------")

def myfunc4(string1):
    res = ""
    for item in range(len(string1)):
        if not item % 2:
            res = res + string1[item].upper()
        else:
            res = res + string1[item].lower()
    return res

print(myfunc4("Anthropomorphism"))