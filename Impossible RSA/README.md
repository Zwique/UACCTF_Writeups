# Impossible RSA

![RSA Diagram](https://github.com/user-attachments/assets/2a3b0c18-9030-4c15-962c-08a67f84b987)

The `RSA.py` file demonstrates the basic mechanism of the RSA encryption algorithm. This challenge revolves around understanding and exploiting the RSA cryptosystem to retrieve the desired plaintext from the given ciphertext.

## Hint #1

This one is tricky! If you understand RSA, you're on the right track. If not, you can [read about RSA here](https://en.wikipedia.org/wiki/RSA_(cryptosystem)). 

By leveraging your knowledge of RSA, you should be able to deduce the key generation, encryption, and decryption steps.

![Complete-steps-of-RSA-algorithm-22-Mathematical-Proof-of-RSA-Algorithm-RSA-computations](https://github.com/user-attachments/assets/20b6ed6d-2809-47ec-8fd5-520dbaa7f90b)

## Hint #2

Consider using an [online RSA decoder](https://www.dcode.fr/rsa-cipher).

1. Input the provided values into the decoder.
2. Decrypt the ciphertext step by step.

![Online RSA Decoder Screenshot](https://github.com/user-attachments/assets/fda491d7-cba4-4c64-beef-1da33cba613a)

### Instructions

1. Enter the ciphertext values one at a time:
   ```plaintext
   ciphertext = 399 792 895 889 500 691 328 656 329 212 188 733 261 420 188 548 261 399 188 717 631 631 407 172
   ```
2. Use the RSA parameters (e.g., modulus `n`, public exponent `e`, private key `d`) provided in the challenge to decode the ciphertext.

> [!NOTE]
> Ensure that you handle the ciphertext in the correct order and format to achieve accurate decryption.

Another option to solve this challenge is simply writing a script to get the flag. Check out the `slv.py`.

### Requirement to execute the code
```pip3 install pycryptodome```

Flag: `uacCTF{RSA_g0d_Y0u_1337}`
