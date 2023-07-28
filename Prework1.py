#Question 1. Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
#def hello_name(user_name):

def hello_name(user_name):
    return f"hello_{user_name}!"

print(hello_name("Syd-the-kid"))





#Question 2. Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds(num1):
    for num1 in range(1, 100):
        if num1 % 2 == 1:
            print(num1)

print(first_odds(0))


#Question 3. Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(list_to_sort):
    sorted_list = sorted(list_to_sort)
    print(sorted_list)
    print(list_to_sort)
    return sorted_list[-1]


list = [9, 8,6,5,1,3,2]
print(max_num_in_list(list))

#  sort the list. 1, 2, 3
#  grab last item
#  example 2 def max_num_in_list(list_to_sort):
#      sorted_list = sorted(list_to_sort)
#      print(sorted_list)
#      print(list_to_sort)
#      length = len(sorted_list)
#      return sorted_list[length - 1:] 
#or could do list_sorted.pop()


# Question 4. Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be boolean Type (true/false).

def leap_year(year):
     if (year % 4 == 0):
         if year % 100 == 0:
             if year % 400 == 0:
                 return True
             else:
                 return False
         else:
             return True
     else:
         return False

def leap_year(year):
    if (year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)):
        return True
    else:
        return False
    

    
print(leap_year(4)) # true
print(leap_year(5)) # false 
print(leap_year(8)) # true
print(leap_year(100)) # false
print(leap_year(200)) # false
print(leap_year(400)) # true
print(leap_year(800)) # true


# Simplified Example of True/False
# car='audi'
# isCar = car == 'bmw'
# print(isCar)
#  odd=[]
# for i in range(1,21):
#     if i % 2 == 1:
#         print(i)


# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

# didn't work:::::: def consecutive_numbers(a_list):
#         sorted_list=sorted(a_list)
#         new_list=len(sorted_list)
#         for x in new_list:
#             if (x + 1):
#                 return True
#             else:
#                  return False

#Question 5.  Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def consecutive_numbers(a_list):

    sorted_list=sorted(a_list)
    for x in range(len(sorted_list)-1):
        if sorted_list[x] + 1 not in sorted_list: 
            print(sorted_list[x]+1)
            return False
    return True
list_1=[1,2,3,4,5,6]
list_2=[1,2,4,5,7,8,9]

print(consecutive_numbers(list_1))
print(consecutive_numbers(list_2))

test=['a','b']
for x in range(len(test)):
    print(x)
    print(test[x])