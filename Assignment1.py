'''
1. Write a program which will find factors of given number and find whether the
factor is even or odd
'''

num = int(input("Enter a number \n"))
print("The factors of ", num, " are: ")
for i in range(1, num + 1):
    if num % i == 0:
        if i % 2 == 0:
            print(i, " Even")
        else:
            print(i, " Odd")

'''
2. Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically
'''
input_string = input("Enter a string : ")
words = input_string.split()
words.sort()
print("The sorted words are:")
for word in words:
   print(word, " ")

'''
3. Write a program, which will find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers 
obtained should be printed in a comma separated sequence on a single line
'''
for num in range(1000, 3000 + 1):
    if num % 2 == 0:
        print(num, end=", ")

'''
4.Write a program that accepts a sentence and calculate the number of letters and digits
'''
str = input("Input a string : ")
digit = 0
letter = 0
for i in str:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        letter=letter+1
print("Number of Letters :", letter)
print("Number of Digits :", digit)

'''
5. Design a code which will find the given number is Palindrome number or not

'''

num = input("Enter a Number : ")
rev = ''.join(reversed(num))
print(rev)
if num == rev:
    print(" The number is a palindrome")
else:
    print("The number is not a palindrome ")

 # or by not using revered function
num = input('Enter any number : ')
val = int(num)
if num == str(num)[::-1]:
    print('The given number is palindrome')
else:
    print('The given number is not a palindrome')



