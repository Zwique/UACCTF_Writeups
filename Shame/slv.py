def decrypt_xor(file_path, xor_key):
    try:
        # Open the file and read the encrypted content
        with open(file_path, 'r') as infile:
            encrypted = infile.read().strip()  # Read and strip newline or extra spaces

        # Decrypt using XOR operation
        decrypted = ''.join(chr(ord(c) ^ ord(xor_key)) for c in encrypted)
        
        # Print the decrypted flag
        print("Decrypted flag:", decrypted)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
decrypt_xor("output.txt", 'X')
