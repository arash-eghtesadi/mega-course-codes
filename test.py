# print 2 ** 3
#
# #----------------------------------------------------------------------------------------------------
#
# str= 'hello'
# print str[-2]
#
# #----------------------------------------------------------------------------------------------------
#
# l = [1, 2, 3]
# print l[2]
#
# l.remove(1)
# print l
#
# #----------------------------------------------------------------------------------------------------
#
# t = ("hello", 1, 3)
# print t
#
# #----------------------------------------------------------------------------------------------------
#
# d = {
#     'name': "Arash",
#     'city': "Montreal",
#     'province': "Quebec"
#     }
# print d
# print 'hi'
#
# #----------------------------------------------------------------------------------------------------
#
#
# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return "Zero division"
#
# print divide(300 , 10)
#
# #----------------------------------------------------------------------------------------------------
#
# age = input("enter your age")
# print age
#
# #----------------------------------------------------------------------------------------------------
#
# names = ["Alex", "John", "Mike"]
# for name in names:
#     if 'A' in name:
#         print name
#
# #----------------------------------------------------------------------------------------------------
#
# def currency_converter(rate, euros):
#     dollars = euros * rate
#     return dollars
#
# r = input("enter rate: ")
# e = input("enter euros: ")
# print currency_converter(float(r), float(e))
#
# #----------------------------------------------------------------------------------------------------
#
# password = ''
# while password != 'python123':
#     password = input("enter password : ")
#     if password == 'python123':
#         print "you are logged in"
#     else:
#         print "sorry, try again"
#
# #----------------------------------------------------------------------------------------------------

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
