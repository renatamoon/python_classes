# how can I read the content of a file (as txt) in python

my_file = open('data.txt', 'r') # here you can see the name of the file and then R is the mode (reading)

file_content = my_file.read()
my_file.close()
"""there's a limit of files that yuu can open at once. That's you have to close it."""

print(file_content)

# ----------------- now you can write too

user_name = input('Enter your name: ')

my_file_writing = open('data.txt', 'w') # on mode of WRITING - delete what's in it and then overwrite
my_file_writing.write(user_name)

my_file_writing.close()