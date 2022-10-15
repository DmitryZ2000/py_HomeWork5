PATTERN = 'абв'
my_text = 'арбуз абвгд был абвгд красным'

print('0', 'арбуз абвгд был абвгд красным')

print('1', my_text.split())

li = [word for word in my_text.split()]
print('2', li)

my_list = list(filter(lambda word: not PATTERN in word, li))

print('3', my_list)

print('4 - Решение Ревьюера', ' '.join([word for word in my_text.split() if not PATTERN in word])) # Решение в 1 строку от преподавателя

print('5', ' '.join(list(filter(lambda word: not PATTERN in word, li)))) # Решение в 1 строку от меня (можно не переводить в строку см ниже)

print('6', ' '.join(filter(lambda word: not PATTERN in word, li))) # Решение в 1 строку от меня (можно не переводить в строку оставлять тип filter)