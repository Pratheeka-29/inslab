def vigenere_cipher(text, key, mode="encrypt"):
    key = key.upper()
    result = ""
    key_index = 0
    shift_direction = 1 if mode == "encrypt" else -1
    
    for char in text.upper():
        if char.isalpha():
            shift = (ord(key[key_index]) - ord('A')) * shift_direction 
           
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)  
        else:
            result += char
    return result

# Example usage
plaintext = "HELLO"
key = "KEY"

# Encrypt
encrypted_text = vigenere_cipher(plaintext, key, "encrypt")
print("Encrypted:", encrypted_text)

# Decrypt
decrypted_text = vigenere_cipher(encrypted_text, key, "decrypt")
print("Decrypted:", decrypted_text)
