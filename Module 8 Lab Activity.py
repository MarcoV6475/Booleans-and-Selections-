#Marco Villegas
#6/2/23

#Problem 1
print("\n\nProgram 1")

x = input('Enter a number: ')
y = input('Enter a number: ')

def isequal(x,y):
    if x == y:
        print('The numbers are equal!')
    else:
        print('The numbers are NOT equal')
isequal(x,y)
#This problem takes a number the user puts and if they are equal it will
#print the first stement an dif they are NOT equal it will print the second
#statemnt. 


    
#Problem 2
print("\n\nProgram 2")

x = int(input('Enter a number: '))
y = int(input('Enter a number: '))

def sumof10(x,y):
    if x + y > 10:
        print('The sum of', x, 'and', y, 'is greater than 10!')
    elif x + y < 10:
        print('The sum of', x, 'and', y, 'is less than 10!')
    else:
        print('The sum of', x, 'and', y, 'is equal to 10!')
sumof10(x,y)
#In this program the user inputs number then if the sums of the numbers is greater
#than 10 it prints statement 1. If sum of x and y is less thna 10 it prints
#statement 2. Lastly, if sum of x and y is equal to 10 it prints statement 3.



#Problem 3
print("\n\nProgram 3")

lst = [1, 36, 65, 3, 41, 5, 67, 25, 9]

def lst5(lst):
    if 5 in lst:
        print('The numebr 5 is on that list!')
    else:
        print('There is NO number 5 on the list')
lst5(lst)
#In this program it checks a list to see if the number 5 is there if it is it will
#print statement 1. If I remove the 5 from the list it will print statement 2. 



#Problem 4
print("\n\nProgram 4")

year = int(input('Enter a year: '))
def leapyear(year):
    if (year % 400 == 0) and (year % 100 == 0):
      print('{0} is a leap year'.format(year))
    elif (year % 4 == 0) and (year % 100 != 0):
        print('{0} is a leap year'.format(year))
    else:
        print('{0} is not a leap year'.format(year))
leapyear(year)
#This program ask's the user to input a year and then it will print the first
#statement if it is a leap year. If the year is goes through the modolus operator
#of 4 and NOT 100 then it prints statement 2. Lastly, if the year is NOT divisble
# by 4 and 100 then it will print statement 3, not a leap year.




#Problem 5
print("\n\nProgram 5")

def task(items, debuffs):
    if "rope" in items and "coat" in items and "first aid kit" in items and "slow" not in debuffs:
        print("You are able to climb mountain")
    if "pan" in items and "groceries" in items and "small" not in debuffs:
        print("You are able to cook a meal!")
    if "pen" in items and "paper" in items and "idea" in items and "confusion" not in debuffs:
        print("You are able to write a book!")

x = ["pan", "paper", "idea", "rope", "groceries"]
y = ["slow"]

task(x,y)
#This programs goes through the lists of "x" and "y" then it will go through the
#if statements and because we are using the "AND" function if one of the statements
#is false then we move on until one statement returns all true; which is cooking
#a meal!
