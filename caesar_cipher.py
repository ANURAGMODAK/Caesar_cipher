def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            # Determine the appropriate case range
            if char.islower():
                start = ord('a')
            elif char.isupper():
                start = ord('A')

            # Apply the shift and wrap around the alphabet
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += char
    return result

# Take user input for the text and shift value
text = input("Enter your text to encrypt: ")
shift = int(input("Enter shift value (integer): "))

# Encrypt the user input
encrypted_text = caesar_cipher(text, shift)
print("Encrypted text is: ", encrypted_text)

# Decrypting the encrypted text
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted text is: ", decrypted_text)