f = open('my_text_script.txt', 'w')
f.write('Hello Wolrd!!')
f.close()


with open('my_text_script.txt', 'r') as f:
    file_data = f.read()
print(file_data)