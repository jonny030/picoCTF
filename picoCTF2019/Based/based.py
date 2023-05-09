from pwn import *

p = remote('jupiter.challenges.picoctf.org',15130)
p.recvuntil('Please give the ')
l = p.recvline().decode().replace(" as a word.","").split(" ")

payload = ""
for item in l:
    payload +=chr(int(item,2))
print(payload)
p.recv()
p.sendline(payload)

p.recvuntil('Please give me the  ')
l = p.recvline().decode().replace(" as a word.\n","").split(" ")
payload = ""
for item in l:
    payload +=chr(int(item,8))
print(payload)
p.recv()
p.sendline(payload)

p.recvuntil('Please give me the ')
l = p.recvline().decode().replace(" as a word.\n","")
print(l)
payload = ""
for index in range(0,len(l),2):
    payload +=chr(int(l[index:index+2],16))
print(payload)
p.recv()
p.sendline(payload)

print(p.recv())
