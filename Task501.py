# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
my_text = 'Скажика дядя ведь не даромабв Москва спалеабвнная пажаром французам отдана'
print(my_text)

my_list = my_text.split()
print(my_list)

for item in  my_list:
    if 'абв' in item:
        my_list.remove(item)

print(*my_list)