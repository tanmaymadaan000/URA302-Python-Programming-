#q1 
# print("Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are")

#q2
# firstName=input("Enter you first name")
# lastName=input("Enter you last name")
# print(lastName,firstName)

#q3
# radius=input("Enter the radius of the circle")
# area=3.14*int(radius)*int(radius)
# print("The area of the cricle of radius",radius,"is",area)

#q4
# color_list=["Red","Green","White","Black"]
# print("First:",color_list[0],"\nLast:",color_list[3])

#q5
# n=int(input("Enter a number:"))
# print(n+n*n+n*n*n)

#q6
# values=input("Enter the values:")
# listValues=values.split(',')
# tupleValues=tuple(listValues)
# print(listValues)
# print(tupleValues)

#q7
# Ctemp=float(input("Enter the temperature in celcius:"))
# Ftemp=(9/5*Ctemp)+32
# print(Ftemp)

#q8
# num1=int(input("Enter First Number:"))
# num2=int(input("Enter Second Number:"))
# num1,num2=num2,num1
# num1+=1
# print("First Number:",num1)
# print("Second Number:",num2)

#q9
# num=int(input("Enter a number:"))
# if(num%2==0):
#     print(num,"is even")
# else:
#     print(num,"is odd")

#q10
# year=int(input("Enter a year to check if its leap or not"))
# if(year%4==0 and year%400==0):
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")

#q11
# import math
# x1=int(input("Enter the x coordinate of first point:"))
# y1=int(input("Enter the y coordinate of first point:"))
# x2=int(input("Enter the x coordinate of second point:"))
# y2=int(input("Enter the y coordinate of second point:"))

# dist= math.sqrt((x2-x1)**2-(y2-y1)**2)
# print("The Euclidean distance between the two coordinates is:",dist)

#q12
# a=int(input("Enter the first angle:"))
# b=int(input("Enter the second angle:"))
# c=int(input("Enter the third angle:"))

# if(a+b+c==180):
#     print("These angles form a Triangle")
# else:
#     print("These three angles do not form a triangle")

#q13
# p=int(input("Enter the principal amount:"))
# r=float(input("Enter the rate of interest in %:"))
# n=int(input("Enter the number of times interest applied per time period:"))
# t=int(input("Enter the number of time period ellapsed:"))
# amount=p*((1+r/n)**(n*t))
# print("Amount after compound interest:",amount)

#q14
# num=int(input("Enter a number:"))
# count=0
# for i in range(2,num//2+ 1):
#     if(num%i==0):
#         count+=1
# if(count>0):
#     print(num,"is not prime")
# else:
#     print(num,"is a prime number")

#q15
# num=int(input("Enter a number:"))
# sum=0
# for i in range(num+1):
#     sum+=i*i
# print("Sum:",sum)