txt = open("new.txt", 'r')
char = txt.read()
txt.close()

char = char.replace('java', 'python')

txt = open("new.txt", 'w')
txt.write(char)
txt.close()