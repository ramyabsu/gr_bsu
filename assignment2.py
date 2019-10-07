# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 01:05:33 2019

@author: Ramya
"""
'''
1. What is the output of the following code?
nums = set([1,1,2,3,3,3,4,4])
print (len(nums))
Hint: Set consists unique element.

Answer: 4
'''

'''
2.	What will be the output?
d = {"john":40, "peter":45}
print(list(d.keys())

Answer: [‘john’, ‘peter’]    # gives only the keys

'''

'''
3. A website requires a user to input username and password to register. Write a program to check the validity of password given by user. Following are the criteria for checking 
password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
'''
import re

password = input("Enter a password : ")
flag = 0
while True:
    if (len(password) < 6):
        flag = -1
        break
    elif(len(password)>12):
        flag = -1
        break
    elif not re.search("[a-z]", password):
        flag = -1
        break
    elif not re.search("[A-Z]", password):
        flag = -1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[$#@]", password):
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
if flag == -1:
    print("Not a Valid Password")


'''
 4. Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9] 
Hint: Use Loop to iterate through list elements
'''

my_list = [4,7,3,2,5,9]
list_enu = enumerate(my_list)
for index, value in list_enu:
    print(index, value)

'''
5.	Please   write   a   program   which accepts  a   string   from   console   and   print   the characters that have even indexes.
Example: If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be: Helloworld
'''
my_str = input("Enter a string : ")
str_enu = enumerate(list(my_str))
new_str = []
for index, value in str_enu:
    if index % 2 == 0:
        #new_str= new_str + list(value)
        new_str.append(value)
print(''.join(new_str))

'''
6.	Please write a program which accepts a string from console and print it in reverse order.
Example: If the following string is given as input to the program: 
rise to vote sir Then, the output of the program should be:
ris etov ot esir
'''
my_str = input("Enter a string : ")
rev = ''.join(reversed(my_str))
print(rev)

'''
7.	Please write a program which count and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
'''
input_string = input("Enter a string: ")
temp = ''
for letter in input_string:
    if letter not in temp:
        print(letter, ', ', input_string.count(letter))
        temp = temp+letter

'''
8.	With   two   given   lists   [1,3,6,78,35,55]   
and   [12,24,35,24,88,120,155],   write   a program to make a list 
whose elements are intersection of the above given lists
'''
def intersection_fun(list1, list2):
    return set(list1).intersection(list2)

list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 5]
print(intersection_fun(list1, list2))

'''
9.	By using list comprehension, please write a program to
 print the list after removing the value 24 in [12,24,35,24,88,120,155]
'''
lst = [12, 24, 35, 24, 88, 120, 155]
new_lst = [n for n in lst if n != 24]
print(new_lst)

'''
10.	By using list comprehension, please write a program 
to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]
'''
lst = [12, 24, 35, 70, 88, 120, 155]
new_lst = [x for x in lst if lst.index(x) != 0 and lst.index(x) != 4 and lst.index(x) != 5]
print(new_lst)

#or

lst = [12, 24, 35, 70, 88, 120, 155]
new_lst = [x for (i, x) in enumerate(lst) if i not in (0, 4, 5)]
print(new_lst)
