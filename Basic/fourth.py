# defining function with def 
def greeting():
    print('sharad poddar')

greeting()


# sending an argument
def greeting_1(name, age="28"):
    # notice difference between + and ,
    print('hello'+name,'bye!',age)
    print(f"my name is {name}")

greeting_1('sharad',20)
# auomatically gets value
greeting_1('naman')


# def with input
def greeting_2(age=20):
    name = input()
    print(f"yoho! {name} and age: {age}")

greeting_2(32)


# note that we cant use + in case of an integer, we must use string
# conversion into string by keyword str
num = 20
print(num, type(num))
name_1 = str(num)
print(name_1, type(name_1))


# Excersie
def function(color='red', age=20):
    color = input()
    name = input()
    print(f"We hear you like the color {color.lower()}!")
    print(f"{name.capitalize()},You are {age+1}!")

function()



# function named-notation so that sending argument regardless order
def greeting_3(name, age=20, color='red'):
    print(f"{name},{age},{color}")
    
greeting_3(age=12, name='anyname', color='green')    


# return value function
def value_add_tax(amount):
    price = amount + amount*0.25
    return price

print(value_add_tax(100))
print(value_add_tax(100), type(value_add_tax(100)))


# how to return an value in form of tuple as on receving one in float format
def value_add_tax_1(amount):
    price = amount + amount*0.25
    return amount,price

print(value_add_tax_1(100))
print(value_add_tax_1(100), type(value_add_tax_1(100)))


# returning an list, simliiarly we can returns as tuples or in a format of string
def value_add_tax_2(amount):
    price = amount + amount*0.25
    return [amount,price]

print(value_add_tax_2(100))
print(value_add_tax_2(100), type(value_add_tax_2(100)))
print(value_add_tax_2(100)[1], type(value_add_tax_2(100)[1]))


