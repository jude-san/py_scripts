# creating(if does not exist) and reading a file 
f = open('my_text_script.txt', 'w')
f.write('Hello Wolrd!!')
f.close()

# using 'with' function so that i do not need to use close() for every code.

with open('my_text_script.txt', 'r') as f:
    file_data = f.read()
print(file_data)