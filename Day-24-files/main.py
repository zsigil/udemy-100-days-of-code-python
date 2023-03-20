#OPEN FILE

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     #file.close() #no need to close if we use 'with'


#WRITE TO A FILE
#'w' -overwrite
#'a' -append

with open('my_file.txt', mode='a') as file:
    file.write('This is another line.')


with open('new_file.txt', mode='w') as file:
    file.write('File gets created if already not exists')