from cryptography.fernet import Fernet

# creates a new key and stores it in a new ly created file, keyFile.txt
with open('keyFile.txt', 'wb') as keyFile:
    key = Fernet.generate_key()
    keyFile.write(key)

# reads the new keyFile.txt and assigns it the the variable key
with open('keyFile.txt', 'rb') as readKeyFile:
    key = readKeyFile.read()

# creates an instance of the Fernet class and allows methods for encryption and decryption
f = Fernet(key)

# fill in the .txt file you wish to encrypt
with open('FILEOFYOURCHOICE.txt', 'rb') as file:
    originalText = file.read()

# encrypts your text using the key
encryptedText = f.encrypt(originalText)

# writes the encrypted text to a new file called encryptedFile.txt
with open('encryptedFile.txt', 'wb') as encryptedFile:
    encryptedFile.write(encryptedText)