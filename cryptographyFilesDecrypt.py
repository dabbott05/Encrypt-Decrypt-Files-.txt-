from cryptography.fernet import Fernet

# opens you file with the key included, keyFile.txt, and assigns it to the variable key
with open('keyFile.txt', 'rb') as keyFile:
    key = keyFile.read()

# creates an instance of the Fernet class and allows methods for encryption and decryption
f = Fernet(key)

# opens the file with your encrypted text, encryptedFile.txt, and assigns it to a new variable
with open('encryptedFile.txt', 'rb') as encryptedFile:
    encryptedText = encryptedFile.read()

# decrypts the encrypted file using the key
decryptedText = f.decrypt(encryptedText)

# creates a file with the newly decrypted text
with open('decryptedFile.txt', 'wb') as decryptedFile:
    decryptedFile.write(decryptedText)
