# Shame

<img width="496" alt="Screenshot 2024-12-30 at 21 51 05" src="https://github.com/user-attachments/assets/e8a60570-d2e9-4549-b232-6ec578c9cb6d" />

The `shame.cpp` file explicitly demonstrates the use of the XOR cipher, a basic encryption technique. To understand this better, let’s delve into what the XOR operation is and how it works in the context of encryption and decryption.

### What is XOR?
XOR, short for "exclusive OR," is a logical operation that outputs true (or 1) if and only if the inputs are different. Here is a truth table to illustrate its behavior:

| Input A | Input B | A XOR B |
|---------|---------|---------|
|    0    |    0    |    0    |
|    0    |    1    |    1    |
|    1    |    0    |    1    |
|    1    |    1    |    0    |

This property makes XOR particularly useful in encryption because applying the same operation twice with the same key will reverse the process, effectively decrypting the encrypted data.

![images](https://github.com/user-attachments/assets/1c295ff4-8e93-472d-bd3f-13b960c3e2b9)

### How Encryption and Decryption Work
The XOR cipher operates by applying the XOR operation between the plaintext (original message) and a key. The key must be the same length as the plaintext for the encryption to work effectively. Here are the steps:

1. **Encryption**
   - Each bit of the plaintext is XORed with the corresponding bit of the key to produce the ciphertext.

2. **Decryption**
   - The ciphertext is XORed again with the same key to retrieve the original plaintext.

This double application of XOR ensures data security as long as the key remains secret.

![xor-xor](https://github.com/user-attachments/assets/d1de37e9-2568-4f7e-b732-8bb20e20e4fe)

### Example
Here’s a simple illustration of the XOR cipher process:

#### Example Data:
```plaintext
Original FLAG:  HELLO
Key:            XORKEY
```

#### Encryption:
Each character of the `FLAG` is XORed with the corresponding character of the `KEY`. If the key is shorter than the plaintext, it should typically repeat or cycle to match the length of the plaintext.

```plaintext
FLAG (ASCII):   72 69 76 76 79    (ASCII values of 'H', 'E', 'L', 'L', 'O')
KEY (ASCII):    88 79 82 75 69    (ASCII values of 'X', 'O', 'R', 'K', 'E')
XOR Result:     16 10 30 7 10     (Result of XORing each pair of values)
CIPHERTEXT:     Non-readable binary data or encoded output.
```

#### Decryption:
The ciphertext is XORed again with the same key to recover the original plaintext:

```plaintext
CIPHERTEXT:     16 10 30 7 10
KEY (ASCII):    88 79 82 75 69
Result:         72 69 76 76 79   (ASCII values match the original plaintext)
Recovered FLAG: HELLO
```

This process shows that the XOR operation is symmetrical, and applying the key twice (once for encryption and once for decryption) retrieves the original data.

# Solution
By simply replacing each XORed character with the result of another XOR using the same key, the original plaintext can be easily retrieved. Run ```slv.cpp``` OR ```slv.py``` to receive the flag.

Flag: ``
