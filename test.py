print 2 ** 3

#----------------------------------------------------------------------------------------------------

str= 'hello'
print str[-2]

#----------------------------------------------------------------------------------------------------

l = [1, 2, 3]
print l[2]

l.remove(1)
print l

#----------------------------------------------------------------------------------------------------

t = ("hello", 1, 3)
print t

#----------------------------------------------------------------------------------------------------

d = {
    'name': "Arash",
    'city': "Montreal",
    'province': "Quebec"
    }
print d
print 'hi'

#----------------------------------------------------------------------------------------------------


def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero division"

print divide(300 , 10)

#----------------------------------------------------------------------------------------------------

age = input("enter your age")
print age

#----------------------------------------------------------------------------------------------------

names = ["Alex", "John", "Mike"]
for name in names:
    if 'A' in name:
        print name

#----------------------------------------------------------------------------------------------------

def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars

r = input("enter rate: ")
e = input("enter euros: ")
print currency_converter(float(r), float(e))

#----------------------------------------------------------------------------------------------------

password = ''
while password != 'python123':
    password = input("enter password : ")
    if password == 'python123':
        print "you are logged in"
    else:
        print "sorry, try again"

#----------------------------------------------------------------------------------------------------

names = ["Alex", "John", "Mike"]
email_domain = ['gmail', 'yahoo', 'hotmail']

for i, j in zip(names, email_domain):
    print i, j

#----------------------------------------------------------------------------------------------------

class first:
    def setdata(self, value):
        self.data = value

    def getdata(self):
        print 'from first ', self.data

# inheritance
class second(first):
    #overriding
    def getdata(self):
        print 'from second ', self.data

    def message(self):
        print 'object oriented programming'

x = first()
x.setdata(10)
x.getdata()

y = second()
y.setdata('hi')
y.getdata()

#----------------------------------------------------------------------------------------------------

class student():
    def student_name(self, name):
        self.name = name
    def qualification(self):
        return 'student'
    def display(self):
        print self.qualification()

# inheritance
class eng_student(student):
    # polymorphism
    def qualification(self):
        return 'engineering student'

bob = student()
bob.student_name('Bob')
bob.display()

mike = eng_student()
mike.student_name('Mike')
mike.display()

#----------------------------------------------------------------------------------------------------

# scope

# global variable
x = 10

def f():
    # local variable in method
    x = 20

class c:
    # class variable
    x = 30

#----------------------------------------------------------------------------------------------------


def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message

greet = compose_greet_func()
print greet()

#----------------------------------------------------------------------------------------------------

def f1(name):
    def f2():
        return "Hello " + name

    return f2

greet = f1("John")
print greet()

#----------------------------------------------------------------------------------------------------

# # function decorator
def f1(name):
   return "Hello {0}, welcome to our site".format(name)

def p_decorate(func):
   def f2(name):
       return "<p>{0}</p>".format(func(name))
   return f2

my_text = p_decorate(f1)

print my_text("John")

#----------------------------------------------------------------------------------------------------

# function decorator
def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


def get_text(name):
   return "Hello {0}, welcome to our site".format(name)

my_text = div_decorate(p_decorate(strong_decorate(get_text)))

print my_text("John")

#----------------------------------------------------------------------------------------------------

# function decorator
def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper


def get_text(name):
   return "Hello {0}, welcome to our site".format(name)

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
   return "Hello {0}, welcome to our site".format(name)

print get_text("John")

#----------------------------------------------------------------------------------------------------

# method decorator
def p_decorate(func):
   def func_wrapper(self):
       return "<p>{0}</p>".format(func(self))
   return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name + " " + self.family

my_person = Person()
print my_person.get_fullname()

#----------------------------------------------------------------------------------------------------

# passing arguments to decorators
def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


@tags("p")
def get_text(name):
    return "Hello " + name

print get_text("John")

#----------------------------------------------------------------------------------------------------

# memorize decorator
'''
    A function decorated with @Memorize caches its return
    value every time it is called. If the function is called
    later with the same arguments, the cached value is
    returned (the function is not reevaluated). The cache is
    stored as a .cache file in the current directory for reuse
    in future executions. If the Python file containing the
    decorated function has been updated since the last run,
    the current cache is deleted and a new cache is created
    (in case the behavior of the function has changed).
 '''
def memoize(function):
  memo = {}
  def wrapper(*args):
    if args in memo:
      return memo[args]
    else:
      rv = function(*args)
      memo[args] = rv
      return rv
  return wrapper


@memoize
def fibonacci(n):
  if n < 2: return n
  return fibonacci(n - 1) + fibonacci(n - 2)


import timeit
start_time = timeit.default_timer()
# code you want to evaluate
print fibonacci(50)

print "It took this much time to execute : "
elapsed = timeit.default_timer() - start_time

print elapsed

#----------------------------------------------------------------------------------------------------

'''
We use lambda functions when we require a nameless function for a short period of time.
In Python, we generally use it as an argument to a higher-order function
(a function that takes in other functions as arguments).
Lambda functions are used along with built-in functions like filter(), map() etc.
'''
# filter function, lambda function
# filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print new_list

#----------------------------------------------------------------------------------------------------

# map function, lambda function
# double each item in a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))

print new_list

#----------------------------------------------------------------------------------------------------

