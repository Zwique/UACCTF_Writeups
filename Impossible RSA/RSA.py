# Given string
flag = "uacCTF{Fake_Flag}"


# Convert each character to its ASCII value and store them as integers in a list
decimal_values = [ord(char) for char in flag]

e = 3
p = 23
q = 41
n = p * q

# RSA encryption: c = m^e % n
for i in decimal_values:
    c = pow(i, e, n)

    print(c, end=' ')

#Output: 399 792 895 889 500 691 328 656 329 212 188 733 261 420 188 548 261 399 188 717 631 631 407 172