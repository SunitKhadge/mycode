#!/usr/bin/python3

count = 0

#read content of dracula as afile object
with open('dracula.txt', 'r') as dracula:
    with open('spookyloop.txt', 'w') as spookyloop:    
        #loop over each line and print
        for line in dracula:
            if 'vampire' in line.lower():
                print(line)
                #increase count by 1
                count +=1

print (count)

