# user input
name = input('what is your name ')
print('hello '+name+' !')
age = input('what is your age ')
print(f'{age} is your age')

# type-casting
num1 = input('Enter num1 ')
num2 = input('Enter num2 ')
print(int(num1) + int(num2))

# roud to number of decimal
num_1 = 1.2345678
print(num_1)
print(round(num_1,2))    # here we round uptil only two decimal place

# lists
# simmialr to array
# negative indexed also works here as negative revrse the things
friends = ['sharad','josh','john','terry','messi','john']
print(friends)
print(friends[1])

# length of list
print(len(friends))

# finding index
print(friends.index('messi'))

# number of occ
print(friends.count('john'))

# list with int
numbers = [1,5,4,2,7,9]
print(numbers)

# sort int list
numbers.sort()      # it changes original list
print(numbers)

# sorting in reverse order
numbers.sort(reverse=True)
print(numbers)

# sorting strings list by letters
friends.sort()      # this will sort according to the starting letter
print(friends)

# revsres an strings list
friends.reverse()
print(friends)

# casual 
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(max(friends))
print(min(friends))
# print(sum(friends))  this will not work as strings sum no meaning

# adding another memeber to the lists
friends.append('hello')
print(friends)
friends.insert(2,'hello_2')  # insert at certain point
print(friends)

# adding two list 
friends.extend(numbers)
print(friends)

# remove specified element
friends.remove('messi')
print(friends)

# pop something
# we can also specified what we want pop
friends.pop()
print(friends)

# empty the list
friends.clear()
print(friends)

# delete list completely
del friends
# print(friends)  here friends is not defined
# we can delete specific element also in list

# ways of copying the lists
new_numbers = numbers[:]
print(new_numbers)
print(numbers)

new_numbers_1 = numbers.copy()
print(new_numbers_1)

new_numbers_2 = list(numbers)
print(new_numbers_2)



