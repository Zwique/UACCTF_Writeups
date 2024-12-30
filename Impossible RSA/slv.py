from Crypto.Util.number import inverse

# Ciphertext array representing the encrypted message
ciphertext = [399, 792, 895, 889, 500, 691, 328, 656, 329, 212, 188, 733, 261, 420, 188, 548, 261, 399, 188, 717, 631, 631, 407, 172]

# Public exponent used in RSA encryption
e = 3

# Two prime numbers used for key generation
p = 23
q = 41

# Modulus for RSA, product of primes
n = p * q

# Step 1: Calculate the Euler's totient function (phi)
phi = (p - 1) * (q - 1)  # phi = (p-1)(q-1)

# Step 2: Compute the private decryption key (d)
# The decryption key is the modular multiplicative inverse of e mod phi
d = inverse(e, phi)
print("Decryption key:", d)

# Step 3: Decryption process
# Loop through each encrypted value in ciphertext
flag = ''
for i in ciphertext:
    # Apply RSA decryption formula: decrypted_text = (i^d) mod n
    decrypted_text = pow(i, d, n)
    # Convert the decrypted numerical value to its corresponding ASCII character
    flag += chr(decrypted_text)

# Output the decrypted flag
print(f"Flag is {flag}")
