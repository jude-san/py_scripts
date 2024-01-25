##### creating(if does not exist) and reading a file 
# f = open('my_text_script.txt', 'w')
# f.write('Hello Wolrd!!')
# f.close()

#### using 'with' function so that i do not need to use close() for every code.

# with open('camelot.txt', 'w') as f:
#     f.write('We\'re the knights of the round table\n We dance whenever we\'re able\n')
# print(file_data)

####  using arg parameters in .read() function to explore how it read file. 
# with open('camelot.txt', 'r') as text:
#     print(text.read(2))
#     print(text.read(8))
#     print(text.read())

##### using loops to iterates over each lines

camelot_lines = []
with open('camelot.txt') as f:
    for line in f:
        #### ["We're the knights of the round table\n", "We dance whenever we're able\n"] the output includes \n whicg is not needed for most cases, in other to remove the newline use .split()
        camelot_lines.append(line)
        #### using .split() to remove newline from output
        camelot_lines.append(line.split())

print(camelot_lines)