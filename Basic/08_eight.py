# file is opend by defult read and text mode
f = open('demo.txt')
print(f.read())

# file is opened in read and text mode
# If the file is located in a different location, you will have to specify the file path
f = open('demo.txt', 'rt')
print(f.read())
# it will read only first 5 characters
# create a buffer value problem so i commeted above one or it will be next characters
print(f.read(4))


f = open("demo.txt", "r")
# line1
print(f.readline())
# line2
print(f.readline())


# append will add on text
f = open("demo.txt", "a")
f.write(" Now the file has more content!")
f.close()
f = open('demo.txt','rt')
print(f.read())
f.close()


# write will overwrite text
f = open("demo.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open('demo.txt','rt')
print(f.read())
f.close()

# for creating new file
# f = open("myfile.txt", "x")
# create new file if not exist
f = open('secondfile.txt','w')

# to delete the file
import os
# os.remove('myfile.txt')   file already removed

#Check if file exists, then delete it:
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# for deletion of folder we used 
# os.rmdir("folder_name")   we can only remove empty folder
    
# file path
#    windows '\'
#    linus '/' 

# types of path
# 1. Absolute path
#   • Specifies the complete path from the root directory.
#   • It remains constant regardless of the current working directory,
#     providing an exact and fix
    
# 2. Relative path
#   • Specifies the path relative to the current working directory.
#   • It is more flexible because it allows you to move your code or project
#     to another directory without changing all the file paths.
    
#   • Windows Absolute Path: C:\Users\Username\Documents\example.txt
#   • Unix Absolute Path: /home/username/documents/example.txt
#   • Relative Path: ../images/picture.jpg