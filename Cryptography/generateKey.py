# Import the necessary library for encryption
from cryptography.fernet import Fernet

# Set the desired file path where the encryption key file will be saved
file_path = "file path"
extend = "\\"
file_name = "encryption_key.txt"

# Generate a new encryption key using Fernet
key = Fernet.generate_key()

# Open the file in binary write mode and write the key to it
file = open(file_path + extend + file_name, 'wb')
file.write(key)
file.close()

