# reg ex
# reg ex reffered to regular expression, used for matching patterns in string, symbol, numbers.

# ^ matches begging of line
# $ matches end of line
# . matches any char
# \s matches whitespace
# \s maches any non-whitespace char
# * repeats a char zero or more times
# *? repreas char zero or more times(non greedy)
# + repeat char one or more times
# +? non greedy
# [aeious] matches a single char in the listed set
# [^XYZ] matches a single char not in listed set
# [a-z0-9] a set of char includes in range
# ( indicates when string extraction start
# ) indication when string extraction end

import re

# without any ragx
line = 'my name From: sharad'
line = line.rstrip()
if line.find('From:') >=0:
    print(line)
    

# with ragx
# it returns true/false
if re.search('From:',line):
    print(line)



# re.findall()
# extranting the string
# getting all the thing mathes in b/w [0-9]
# returns in fall of list
y = re.findall('[0-9]',line)
print(y)    
line = 'my 2 favourite numbers are 10 and 7'
y = re.findall('[0-9]',line)
print(y)    
y = re.findall('[aeiou]',line)
print(y)



# Greedy match, it work as longest string as output
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)


# non Greedy match, it work as a least string as output
x = 'From: Using the : character'
y = re.findall('^F.+?:',x)
print(y)


# for real character in string
x = 'we just received $10.00 for cookies'
y = re.findall('\$[0-9].',x)
print(y)
y = re.findall('\$[0-9][0-9]',x)
print(y) 
y = re.findall('\$..',x)
print(y)
