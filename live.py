# from typing import List


# List=['mon','tue','wed','thur','fri','sat','Sun']
# string=''.join(List)
# print(string)

# from re import I


# def iterate():
#     i=0
#     while i<=10:
#         prev_number=i
#         sum=prev_number+i
#         print(f"The previous number is {i} the previous number is {prev_number} and the sum is {sum}")
        
# iterate()
# # finding the nuber that iterates through the first 10numbers in each itration prints the sum of current and previous num
# def iterate():
#     x=range(1,11)
#     for n in x:
#         y=n-1
#         sum= n+(n-1)
#         print(f"the current number is {n} previous is {n-1}8 and sum is {sum}")  
# iterate()
# # how many times monday appears in this list
# def days():
#     x=['Sun','Mon','Tue','Wed','Thur','Fri','Sat','Mon','Mon']
#     print(x.count('Mon'))
# days()

# # returning the elements of the negative indexes
# def list_of_names():
#     y=["chris","jack","john","daman"]

#     print("The negative index of",y[-1] ,'is', y.index("daman"))
#     print(y[-1])
# list_of_names()

# # getting the 
# def name():
#     x="Juliet"
#     y=(len(x)//2)
#     print(f"the first charater is {x[0]},the middle character is {x[y]},the last character is {x[-1]}")
# name()

# printing the smallest to largest
# def smallest():
#     i=[30,60,1,20,32]
#     i.sort()
#     print(i[0])
# smallest()

# def smallest():
#     x=[30,60,1,20,32]
#     smallest=0
#     for b in x:
#         if b<smallest:
#             print (smallest)
# smallest()


# def numbers():
#   a=[10,20,30,40,50,60]
#   b=[20,80]
#   if b in a:
#       print("true")
#   else:
#       print("false")
# numbers()

# def numbers():
#     a=[10,20,30,40,50,60]
#     b=[20,80]
#     for x in (a,b):
#         if x==a and x==b:
#             print("true")
#         else:
#             print("false")
# numbers()
# from ast import If


# def numbers():
#     a=[10,20,30,40,50,60]
#     b=[10,80]
#     W=(set(a).intersection(set(b)))
#     if W=="set()":
#         return False
#     else:
#         return True
# numbers()

# # finding the nth number
# from operator import truediv


# def numbers(nth):
#  for x in numbers:
#     if x==nth:
#         return "true"
#     else:
#         return "false"
# numbers([1,2,3,4])

# # removing duplicates in a list
# def numbers():
#     list=[3,5,2,1,6,8,2,3]
#     y=[]
#     for i in list:
#         if i not in y:
#             y.append(i)
#     print(y)
# numbers()

# def fruits():
#     a=["orange","mango","pineapple","kiwi","jackfruit"]
#     a.sort()
#     print(a)
# fruits()

# from audioop import reverse


# def names():
#      a=["orange","mango","pineapple","kiwi","jackfruit"]
#      a.sort()
#      a.reverse()
#      print(a)
# names()

# # sort the list based on how close the number is to 50

# a=[100,50,65,82,23]

# valueOne = 5 ** 2
# valueTwo = 5 ** 3

# print(valueOne)
# print(valueTwo)

# for x in range(0.5, 5.5, 0.5):
#       print(x)

# var= "James Bond"
# print(var[2::-1])

# var = "James" * 2  * 3
# print(var)
# def calculate (num1, num2=4):
#       res = num1 * num2
# print("res")

# calculate(5, 6)

# for i in range(10, 15, 1):
#       print( i, end=', ')

# x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)

# salary = 8000

# def printSalary():
#   salary = 12000
#   print("Salary:", salary)
  
# printSalary()
# print("Salary:", salary)

# var1 = 1
# var2 = 2
# var3 = "3"

# print(var1 + var2 + var3)

# sampleList = [10, 20, 30, 40, 50]
# sampleList.pop()
# print(sampleList)

# sampleList.pop(2)
# print(sampleList)

# resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
# print(resList)

# sampleList = [10, 20, 30, 40]
# del sampleList[0:6]
# print(sampleList)

# aList = [5, 10, 15, 25]
# print(aList[::-2])

# listOne  =  ['a', 'b', 'c', 'd']
# listTwo =  ['e', 'f', 'g']
# newList=[]
# newList = listOne.extend(listTwo)

# my_list = ["Hello", "Python"]
# print("-".join(my_list))

# list1 = ['xyz', 'zara', 'PYnative']
# print (max(list1))

#square of a list of numbers

# aList = [1, 2, 3, 4, 5, 6, 7]
# pow2 =  [x**2 for x in aList]
# print(pow2)



# for num in range(-2,-5,-1):
#     print(num, end=", ")

# x = 0
# while (x < 100):
#   x+=2
# print(x)

# for l in 'Jhon':
#        if l == 'o':
#         pass
#        print(l, end=", ")

# list=["mon","tue","wed","thur","fri"]
# n=set(list)
# print(n)


# #create a list
# my_list = ['Rice', 'Potato', 'Tomato']
 
# #convert the list using set
# se = set(my_list)
 
# #display the set
# print(se)

# def Average(l): 
    
#     avg = sum(l) / len(l) 
#     return avg
  
# my_list = [2,4,6,8,10] 
# average = Average(my_list) 
  
# print(average)


# listy=int(input("Enter numbers"))
# sum=0
# for i in listy:
#     sum+=i
#     average=sum//len(listy)  
#     print(average)   
  
# num = int(input('How many numbers: '))
# total = 0
 
# for n in range(num):
#     numbers = float(input('Enter the number : '))
#     total += numbers
 
# avg = total/num
# print('Average of ', num, ' numbers is :', avg)

# d = {"getrude": 60, "clare": 21}
# f={"julliet":92,"naka":21}

# if "naka" in d:
#     print("already exists")
# else:
#     print("does not exist")


# def checkKey(dict, key):
   
#     if key in dict.keys():
#         print("Present")
#     else:
#         print("Not present")
  
# dict = {'a': 100, 'b':200, 'c':300}
  
# key = 'a'
# checkKey(dict, key)
  
# key = 'r'
# checkKey(dict, key)

# list=[2,33,7,8,100,7,4]
