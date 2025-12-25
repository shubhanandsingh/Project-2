# #This is my first python program
# #print("welcome python to my life")
# print("it's really good")

# first_name = "Bro"
# print(first_name)

# print(f"hello{first_name}")

# food = "pizza"
# print(f"hello bro you like{food}")
# email = "subhanandsingh"

# print (f"your emain is {email}")

# share_price = 339.5
# print(f"the share price was{share_price}")
# gpa = 5.555
# print(f"your gpa is {gpa}")

# is_student = True
# print(f"are you a student? {is_student}")

# plc_is_good = True

# if Plc_is_good:
#     print("plc is good for automation")
# else:
#     print("plc is not good for automation")

# for_sale = True
# if for_sale:
#     print("item is available for sale")
# else:
#     print("item is not available for sale")

#//////////////////////////////////////////////////////////////////////////////////////////
# for types of data
# # String " shubh annad singh"
# Integer = 44
# Float 
# Boolean
#//////////////////////////////////////////////////////////////////////////////////////////////////////

# name = "shubh anand singh"
# age = 25
# gpa = 4.4
# is_student = True

# print(type(age))
# print(type(name))
# print(type(is_student))

# gpa = int(gpa)
# print(gpa)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////using input from user
# name = input("Enter your name")
# if type(name) is str:
#     print(f"my name is {name}")
#     age = input("Enter you age")
#     age = int(age)
#     if type(age) is int:
#         print(f"your age is {age}")
#     else:
#         print("Enter your age not name")
# else:
#     print("Enter your name correctly")

# #////////////////////////////////////////////////////////////////////////////   Here data type already defined (typecasting)
# name = str(input("enter your name"))
# age = int(input("enter your age"))
# print(f"{name} YOur age is {age} years")

# #///////////////////////////////////////////////////////////////////////////    CAlculating the area of rectangle
# length = int(input("Enter the length"))
# widht = int(input("Enter the width"))
# area = length*widht
# print(f"The area of rectangel is {area}")

# import math

# print(math.pi)
# # print(math.e)
# # x =9
# # result = math.sqrt(x)
# # print(result)

radius = float(input("Enter the radius of circle"))
area = math.pi * pow(radius, 2)
print(area)