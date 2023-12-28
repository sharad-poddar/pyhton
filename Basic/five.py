# comparisions and boolean
print(5 == 7)
print(True == False)
print(7 >= 3)
print('o' in 'john')
print('o' not in 'sharad')


a = [23, 37, 89]
b=a
print(b == a)
print(a is b)
# returning an memory, which is same as b is refrence name of a
print(id(a), id(b))


print(int(False))
print(bool(True))
print(bool(''))

# if else stamnets
print('condition: IF statments')
is_morning = False
is_cold = True
if(is_morning or is_cold):
    print('this is morning')
else:
    print('this is night')    


# more complex, intendation is important here
if(is_morning and is_cold):
    print('morning and cold')
elif(not is_morning and is_cold):
    print('night and cold')    
else: 
    print('it is hot')




