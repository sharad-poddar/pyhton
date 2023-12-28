# dictionary -> key,value pairs
# key as a string
# key can also as a number/int
# key is always an unique
movie = {
    'name':'sharad',
    'dob':'2003',
    'cast':'hindu',
}

print(movie)
print(movie['name'])
print(movie['dob'])
print(movie['cast'])

# it replace error ny none or not found
print(movie.get('name'))
print(movie.get('hello','not found'))

# chainging values 
movie['name'] = 'abything'
print(movie)

# updating the movie
movie.update({'name':'all','dob':'2023','cast':'none'})
print(movie)

# removing an elemnt from movie
movie.pop('cast')
print(movie)

# length of no of entries of dic
print(len(movie))

# checking if present or not
print('name' in movie)
# here the forward slash make it as a simple char
if 'namee' not in movie: 
    print('it\'s not in movie')

# copping dic
people = {}
people.update(movie)
print(people)    

movie_1 = {'sharad':'hello'}

# conacting dic in one by update
people.update(movie_1)
print(people)
