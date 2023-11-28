# tuples
# it is immutable like string
friends = ('josh', 'john', 'sharad')
print(friends)
print(friends[0:1])   # here 1 is excluded, print in form of tuple
print(friends[0]) # simply accessig the first element of tupel

# in tuples iterations and searching is faster then list
# we dont use i++ and friends[i] directly i
for i in friends:
    print("** "+ i + " **")


# change in the tuple
# friends[1] = 's_sharad' it gives error
print(friends)

#sets 
friends_sets = {'sharad', 'poddar', 'right', 'left'}
print(friends_sets)
friends_sets_1 = {'right', 'left'}
print(friends_sets.intersection(friends_sets_1))    # print in the form of set

# an empty set always be fullfill by its object
set_1 = set()
print(set_1)

# checking if sharad is in set
print('sharad' in friends_sets)
if 'sharrad' in friends_sets:
    print('hello')
else:
    print('why')    

# union of two set
set_1_1 = {'hello'}
set_2_2 = {'world'}    
print(set_1_1.union(set_2_2))
print(set_1_1 & set_2_2)   # intersection
print(set_1_1 | set_2_2)   # union

# we can subtrcat 1 set from another
print(set_1_1.difference(set_2_2))
print(set_1_1 - set_2_2)
# symmetric diff, it will give the diff of both
print(set_1_1.symmetric_difference(set_2_2))
print(set_1_1 ^ set_2_2)


# duplicates of list
dupli_set = set(set_1_1)
print(dupli_set)

# functions
# setting up the value prely
def greet(name, age=26):
    print('hello world')
    print(f'{name} and {age}')

greet('sharad', 32);    
greet('hello')

