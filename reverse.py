# def reverse(word):
#     str=""
#     for i in word:
#         str=i +str

#     return str
# print(reverse("Julliet"))

# l=[2,4,6,8,10,12,14]
# for i in l:
#     print(i**2)

# a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
# d_items = a_dict.items()
# print(d_items)

# prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for key in prices.keys():
#     if key == 'orange':
#         del prices.keys()

# incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# total_income = 0.00
# for value in incomes.values():
#     total_income += value

# a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# new_dict = {} 
# for key, value in a_dict:
#     if value <= 2:
#         new_dict = value
        
# a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# new_dict = {}
# for key, value in a_dict.items():
#     new_dict[value] = key
    
a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {} 
for key, value in a_dict.items():
    if value <= 2:
        new_dict[key] = value

