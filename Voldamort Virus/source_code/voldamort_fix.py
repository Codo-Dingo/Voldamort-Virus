import os,time
from cryptography.fernet import Fernet
files = []

key = "N2Q30S2gxxCA83cyiDgr3HtXbdUW69XMlaUSCN_QDpw="
for file in os.listdir():
    if file not in ["voldamort.py","TheKey.key","voldamort_fix.py","voldamort.exe","voldamort_fix.exe"]:
        if os.path.isfile(file):
            files.append(file)

password = "Teri Chain Chain"
user_entry = input("Enter the password :- ")
if password == user_entry:

    for file in files:
        with open(file,"rb") as fh:
            contents = fh.read()
        decrypted_data = Fernet(key).decrypt(contents)
        with open(file,"wb") as the_file:
            the_file.write(decrypted_data)
    print("Congrats ! your Files are back now . ^-^")
else:
    print("No Key Found !")

close = input("type 'e' to exit :- ")

    
