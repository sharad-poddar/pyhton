# shelve is library as a dictionary
# sheve used to stores complex data structures and get it back on need
# dictionary like interface

# open or create file
import shelve
f = shelve.open('gfg')

# creating list 
num = [1,2,3,4,5]

# storing data structures
f['num'] = num

# closing the shelve file
f.close()

# retriving data
f = shelve.open('gfg')
num = f['num']
print(num)

# updating data
f['num'] = [1,6,7,8,9]
num = f['num']
print(num)

# to make changes permanent
# simillar to github
f.sync()

# getting keys only means nums
keys = list(f.keys())
print(keys)

# delete data structure
del f['num']
print(list(f.keys()))
f.close()


# Drawbacks of shelve:
#   • It does not support concurrent writes.
#   • It cannot be used to store objects that cannot be handled by pickle.

# application
# 1. data persistence -> storing the computation of program
# 2. configuration setting -> helps to change the data easily and retrive back easily
# 3. caching -> storing the api which reduces expense
# 4. logging -> easy to organize data and analyse them
# 5. session managment -> maintain userdata across diff platforms
# 6. scripting -> alternative to full fledge db
