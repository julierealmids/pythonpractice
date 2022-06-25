# printing the square of numbers in a new list
new_list=[1,2,3,4,5,6,7,100]
x=[]
for x in new_list:
    y=x*x
    print([y])
    
aList = [1, 2, 3, 4, 5, 6, 7]
pow2 =  [x**2 for x in aList]
# print(pow2)

number1=int(input("Enter a number"))
number2=int(input("Enter a number"))
if number1==number2:
    print("true")
else:
    print("false")
    
def nums(a,b):
    sum=a+b
    if sum>5:
        print("greater than 5")
    elif sum<5:
        print("less than five")
    elif sum==5:
        print("equal to 5")
    else:
        print("not valid")
nums(1,2)
nums(9,4)
nums(1,3)

def numbers(a,b):
    sum=a+b
    if sum>5:
        print(f"{sum} is greater than five")
    elif sum<5:
        print(f"{sum} is less than five") 
    elif sum==5:
        print(f"{sum} is equal to five")    
numbers(10,12) 
numbers(1,2) 
numbers(3,2) 
        
def numbers():
    num1=("Enter number")
    num2=("Enter number")
    sum=num1+num2
    if sum>5:
        print(f"{sum} is greater than five")
    elif sum<5:
        print(f"{sum} is less than five") 
    elif sum==5:
        print(f"{sum} is equal to five")


def integers():
    i=[12,34,56,7,89,1,3]
    i[0],i[-1]=i[-1],i[0]
    print(i)    
integers()

def numbers():
    i=input("Enter number")
    z=input("Enter number")
    sum =i+z
    if sum >10:
        print(f"{sum} is greater than 10")
    elif sum <10:
        print(f"{sum} is less than 10")
    elif sum==10:
        print(f"sum is equal to 10")
numbers()
def elements():
   a=['apples', 'pens', 'candy', 'notepad', 'brushes', 'paint']
   print(min(a))
   print(max(a))
   print(a[:3])
   print(a[5:])
elements()
list3 = ["kyle", "darius", "janna", "set", "annie", "warwick", "bauuuuuu"]
print(max(list3))
print(min(list3))

def natural_numbers():
    f=int(input("Enter range: "))
    while (f!=0):
        print(f,end=" ")
        f=f-1
# natural_numbers()

def numbers():
    number = int(input("Enter the input Range : "))
    for iter in range(1,number):
        for i in range(2,iter):
            if (iter%i==0):
                break
    else:
        print(iter)
numbers()

def names():
    l=["summy","juliet","nakayiza"]
    if "martin" in l:
        print("true")
    else:
        print("false")
names()

def square():
    dict={i:i**2 for i in range(1,15)}
    print(dict)
square()

dict_1={}
list_one=[1,2,3,4,5,6,7]
list_two=[1,2,3,8,9,0,2]
for key,value in zip(list_one,list_two):
    if key not in dict_1:
        dict_1[key]=value
    else:
        dict_1=key.update(value)
print(dict_1)

mylist = ["a", "b", "b", "c", "a"]
mylist = sorted(set(mylist))
print(mylist)

# program to sum up numbers in a list
numbers = [1,2,3,4,5,1,4,5] 
Sum = sum(numbers) 
print(Sum)  
Sum = sum(numbers, 10) 
print(Sum)


def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
    return final
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))

from optparse import Values

def values():
    dict={"juliet":22,"nakayiza":21,"apio":23}
    i=dict.values()
    print(max(i))
    print(min(i))
values()

# min and max of dict - values
dict1 = {'key 1': 200, 'key 2': 300}
val = dict1.values()
max = max(val)
min = min(val)
print(min)
print(max)

# checking if a dictinary is empty or not

# checking if a dict is empty
a={}
if len(a)==0:
    print("Dict is empty")
else:
    print("Dict is not empty")

# program to choose a random item from a list        
def values():
    f={"Julliet",21,"Nakayiza",23}
    y=f.values()
if 21 in y:
    print("Not in dictionary")
else:
    print("In Dictionary")
values()

# sorting dictionary values
dict1={"apples":2,"mangoes":4,"oranges":3}
val=dict1.keys()
sort=dict.sort_by_key(val)
print(sort)

# checking if a key exists in a dictionary
a={"mw",5,"you",4,"them",7}
if "mw" in a:
    print("exists")
else:
    print("does not exist")

# mapping a dict
a=["mango","apple"]
b=["yellow","red"]
dict=dict(zip(a,b))
print(dict)

# removing duplicates fro a list
x=[1,3,2,4,2,6,3,8,7,1]
y=[]
for i in x:
    if i not in y:
        y.append(i)
else:
    pass
print(y)

#a program to iterate over dictionary items using for loop.






 

    

    

    
    
                
    
        
            




