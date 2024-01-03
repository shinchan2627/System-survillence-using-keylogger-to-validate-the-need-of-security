# System-survillence-using-keylogger-to-validate-the-need-of-security
Capture keystrokes, system details, and clipboard activity. Periodically record audio and take screenshots for security evaluation. Encrypted logs are sent via email, ensuring remote monitoring. Stop surveillance anytime with Ctrl + Esc. Educational use only; adhere to ethical guidelines and laws.


Introduction:

This project aims to demonstrate the importance of security awareness by implementing a system surveillance tool using a keylogger. The keylogger captures keystrokes, system information, clipboard data, and microphone input. The collected information is then encrypted and sent via email to a designated address.

Disclaimer: This tool is intended for ethical use only. Users are advised to obtain consent and adhere to legal and ethical guidelines before deploying or using this system. Unauthorized use is strictly prohibited.

Features:

Keystroke Logging: Captures user keystrokes for analysis.
System Information: Gathers details about the system, including processor, operating system, and IP addresses.
Clipboard Logging: Records data copied to the clipboard.
Microphone Recording: Captures audio data for a specified duration.
Screenshot Capture: Takes screenshots periodically.
Email Notification: Sends encrypted logs to a specified email address.
User Stop Functionality: Allows the user to stop surveillance using Ctrl + Esc.

Installation:

Ensure Python is installed on your system.
Install the required dependencies by running the following command:
pip install -r requirements.txt
Run the main.py script to initiate surveillance.

Configuration:

Email Settings: Configure the email_address, password, and toaddr variables in main.py with the appropriate email credentials.
Encryption Key: Generate an encryption key using the generateKey.py script in the Cryptography folder.
Usage
Execute main.py to start the surveillance tool.
A warning message will be displayed, indicating that the system is under surveillance.
Press Ctrl + Esc to stop the surveillance at any time.
Encrypted logs will be sent to the specified email address.

Cryptography:

generateKey.py: Generates a new encryption key and saves it to a file.
decryptFile.py: Decrypts the encrypted files and creates a decryption.txt file in the Cryptography folder.

File Organization:

Logs: The captured information is saved in log files, including key_log.txt, systeminfo.txt, clipboard.txt, audio.wav, and screenshot.png.
Encrypted Files: Encrypted versions of log files are stored in Cryptography with filenames prefixed by 'e_'.

Disclaimer:

This tool is intended for educational purposes and security awareness. Any unauthorized use or misuse is strictly prohibited. The developer is not responsible for any legal consequences resulting from the use of this tool without proper authorization.

Note: Always follow ethical guidelines, obtain user consent, and review applicable laws before deploying such tools.

Contributors:

Praveen kumar K
praveenkk418@gmail.com
Feel free to contribute to the project and provide feedback!

License:

This project is licensed under the MIT License.
