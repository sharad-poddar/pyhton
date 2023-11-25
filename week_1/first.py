# no semicolon 
# here double or single commas works
print('welcome to Python 101 in scrimba')
print("sharad")

# variables
# we can only concatenate strings
x = '2'
print('welcome to '+ x +' here!')
# here int works
print('welocme to ',2)

# datatypes int, float, bool, string ...
a = "it's"
b = 123
print('hello '+a+' me!')
print(type(a))
print(type(b))
print(type(1.234))
print(type(True))

# typecasting
x_1 = 23
print(type(x_1))
print(type(str(x_1)))
print(3.5)
print(int(3.5))
print(str(3.5))
print(str("80s"))

item_name = 'widget'
price = 23.5
inventory = 100
is_invetnory = True
print(item_name, price, is_invetnory, inventory)

# common operations
a_1 = 10
b_1 = 20
print(a_1+b_1)
print(a_1*b_1)
# float division
print(a_1/b_1)
# floor division
print(a_1//b_1)
print(a_1-b_1)
print(b_1**a_1)
# module
print(a_1%b_1)

# concat of string
fullName = 'sharad poddar'
print(fullName*2)
print(fullName,fullName)  # it gives space in between
print(fullName+fullName)

# casing of string
name_1 = 'sharad'
print(name_1.upper())
print(name_1)  # it will not change the actual string
print(name_1.lower())

#making first word capitalize
name_2 = 'sharad poddar'
print(name_2.capitalize())

# all beginning letter to be capital
name_3 = 'sharad poddar'
print(name_3.title())

# length of string
name_4 = "sharad_poddar sharad"
print(len(name_4))    # it counts all spaces and _ in string

# if we want to count the letter or word
name_5 = 'Sharad Poddar'
print(name_5.count('Sharad'))
print(name_5.count('a'))

# slicing string
para = "sharad is good boy"
print(para[1])       # start starts from 0
print(para[-1])      # end starts from -1
print(para[2:])      # gettling whole thing after 2
print(para[:2])      # getting whole thing before 2
print(para[2:10])    # limit, her 10 is excluded
print(para.title())  # makes the starting letter of each word bigger
print(para[::2].title())  # takes the every 2nd letter from back
print(para[::-2].title())  # takes the every 2nd leter from start but n revese order
print(para[::-1])  # makes thestring reverse

# string in multiline
namme = """sharad hello how 
are you """
print(namme)

# finding the index of anything
puranamme = "sharad poddar"
print(puranamme.find('poddar'))   # gives the starting index of p
print(puranamme.find('p'))        # gives the starting index of p

# replacment in string
welcomeString = 'hello welcome to python'
print(welcomeString.replace('welcome', 'bye'))  # it actually never changes to orginal string
print(welcomeString)   
welcomeString = welcomeString.replace('python', 'javascript')
print(welcomeString)

randomString = 'sharad '+ 'loves '+'[ '+ 'all the things in world '+ '] '+'!'
print(randomString)
name = 'sharad'
randomString_1 = f'{name} loves [all the things in world] !'  #here f is must
print(randomString_1)
randomString_2 = f'{name} loves [all the things in world] ! {name.upper()}'  #here f is must
print(randomString_2)






