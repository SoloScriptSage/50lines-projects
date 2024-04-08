import random

valid_chars = 'abcdefghijklmnopqrstuvwxyz1234567890'

login_length = random.randint(4, 15);
login = ''

for i in range(login_length):
    pos = random.randint(0, len(valid_chars) - 1)
    login += valid_chars[pos]

if login[0].isnumeric():
    pos = random.randint(0, len(valid_chars) - 10)
    login[0] = valid_chars[pos]

servers = ['@gmail', '@yahoo', '@redmail', '@hotmail', '@bing']
server_pos = random.randint(0, len(servers) - 1)

email = login + servers[server_pos]

tlds = ['.com', '.ro', '.net', '.org']
tld_pos = random.randint(0, len(tlds) - 1)

email += tlds[tld_pos]

print(email)
