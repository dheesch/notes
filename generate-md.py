#!/usr/bin/python3

title = ''
linkText = ''
link = ''
output = ''
counter = 1
directory = input('enter directory: ') 

if(directory[-1] != '/'):
    directory += '/'
print(directory)

readme = open(directory + 'README.md', 'w')

print('Welcome to shitty markdown generator!')
print('enter blank input for title and link to exit')

title = input('Enter Book Title: ')
output += '# ' + title + '\n\n'

while True:

    linkText = input('Enter link title: ')
    link = 'chap' + str(counter) + '.md' 
   
    
    if(linkText == ''):
        readme.write(output)
        readme.close()
        break
    else:
        # write the chapter name on the first line of the chap.md
        chapFile = open(directory + link, 'w')
        chapFile.write('# ' + linkText + '\n\n')
        chapFile.close()

        output += '- [' + linkText + '](' + link + ')\n'
        counter += 1

        


