# Q1

# (i)
# L=[11,12,13,14]
# L.append(50)
# L.append(60)
# print(L)

#(ii)
# L=[11,12,13,14]
# L.remove(11)
# L.remove(13)
# print(L)

#(iii)
# L=[11,12,13,14]
# L.sort
# print(L)

#(iv)
# L=[11,12,13,14]
# L.sort(reverse=True)
# print(L)

#(v)
# L=[11,12,13,14]
# if 13 in L:
#     print("13 is in the list")

#(vi)
# L=[11,12,13,14]
# print(len(L))

# (vii)
# L=[11,12,13,14]
# print(sum(L))

# (viii)
# L=[11,12,13,14]
# print(sum(x for x in L if x % 2 == 1))

# (ix)
# L=[11,12,13,14]
# print(sum(x for x in L if x % 2 == 0))

# (x)
# L=[11,12,13,14]
# sum = 0
# for x in L:
#     if x > 1:
#         flag = True
#         for i in range(2, int(x**0.5)+1):
#             if x % i == 0:
#                 flag = False
#                 break
#         if flag:
#            sum += x
# print(sum)

# (xi)
# L=[11,12,13,14]
# L.clear()
# print(L)

# (x)
# L=[11,12,13,14]
# del L



#Q2
# n = int(input("How many numbers? "))
# numbers = []
# for _ in range(n):
#     num = int(input("Enter a number: "))
#     numbers.append(num)
#     sum=0
# for i in numbers:   
#     sum+=i
    
# print(sum)

# Q3
# arr = [1,2,3,4]
# prod = 1
# for x in arr:
#     prod *= x
# print(prod)

#Q4
# arr=[]
# for i in range(3):
#     layer=[]
#     for j in range(4):
#         row=[]
#         for k in range(6):
#             row.append('*')
#         layer.append(row)
#     arr.append(layer)

# for layer in arr:
#     for row in layer:
#         print(row)
#     print()


#Q5
# (i)
# D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# D[8] = 8.8
# print(D)

# (ii)
# D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# if 2 in D: del D[2]
# print(D)

#  (iii)
# D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# print(6 in D)

# (iv)
# D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# print(len(D))



# v)
# D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# sum=0
# for i in D.values():
#     sum+=i
# print(sum)

# (vi)
# D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# if 3 in D: D[3] = 7.1
# print(D)


# (vii)
# D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
# D.clear()
# print(D)



# Q6
# (i)
# S1 = {10,20,30,40,50,60}
# S2 = {40,50,60,70,80,90}
# S1.add(55)
# S1.add(66)
# print(S1)

# (ii)
# S1 = {10,20,30,40,50,60}
# S2 = {40,50,60,70,80,90}
# S1.discard(10)
# S1.discard(30)
# print(S1)

# (iii)
# S1 = {10,20,30,40,50,60}
# S2 = {40,50,60,70,80,90}
# print(40 in S1)

# (iv)
# S1 = {10,20,30,40,50,60}
# S2 = {40,50,60,70,80,90}
# print(S1.union(S2))

# (v)
# S1 = {10,20,30,40,50,60}
# S2 = {40,50,60,70,80,90}
# print(S1.intersection(S2))

# (vi)
# S1 = {10,20,30,40,50,60}
# S2 = {40,50,60,70,80,90}
# print(S1.difference(S2))


#q7 i)
# import string
# import random
# for i in range(100):
#     len=random.randint(6,8)
#     random_string=''
#     for j in range(len):
#         char=random.choice(string.ascii_letters)
#         random_string=random_string+char
#     print(random_string)

# Q7(ii)
# primes = []
# for n in range(600, 801):
#     if n > 1:
#         flag = True
#         for i in range(2, int(n**0.5)+1):
#             if n % i == 0:
#                 flag = False
#                 break
#         if flag:
#             primes.append(n)
# print(primes)
        
# Q7(iii)
# res = []
# for n in range(100, 1001):
#     if n % 7 == 0 and n % 9 == 0:
#         res.append(n)
# print(res)        
  
        
# Q8
# exam_st_date = (11, 12, 2025)
# print("The examination will start from:", exam_st_date[0], "/", exam_st_date[1], "/", exam_st_date[2])
       

# Q9
# numbers = [10,11,15,23,25,30,42]
# for n in numbers:
#     if n % 5 == 0:
#         print(n)
        
# Q10
# n = 42
# is_even = (n % 2 == 0)
# is_odd = not is_even
# print(n, "is even?", is_even, "is odd?", is_odd)        
        

# Q11
# text = "Emma is my friend. Emma likes reading. EmmaEmma"
# print(text.count("Emma"))


# Q12
# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# new_list = []
# for x in a:
#     if x % 2 == 1:
#         new_list.append(x)
# for x in b:
#     if x % 2 == 0:
#         new_list.append(x)
# print(new_list)


#Q13
# positions = [(2,3), (4,5), (6,7), (7,8)]

# for i in positions:
#     x=i[0]
#     if(x%2==0):
#         print(i)


# Q14
# sensor_data = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
# for id, reading in sensor_data.items():
#     if(reading>3):
#         print(id,reading)


# Q15
# commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
# commands_executed = {"MOVE", "TURN_LEFT", "STOP"}
# not_executed = commands_received - commands_executed
# print(not_executed)


