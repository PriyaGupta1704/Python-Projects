import os
from cryptography.fernet import Fernet
#From Crytogrpahy Library we are importing Fernet class
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb")as key_file:
        key_file.write(key)
def load_key():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key
if not os.path.exists("key.key"):
    write_key()
key=load_key()#Storing keys return by function
fer=Fernet(key)#class Fernet to encrypt/decrypt key

def view():
    with open("passwords.txt","r")as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passwd=data.split("|")
            print("User: ",user, "Password: ", fer.decrypt(passwd.encode()).decode())
def add():
    name=input("Enter you Account Name: ")
    pwd=input("Password: ")
    with open("passwords.txt","a")as f:
        f.write(name+ "|" + fer.encrypt(pwd.encode()).decode()+"\n")
while True:
    mode=input("Would you like to add a new password or view(View/Add),press q to quit ").lower()
    if mode=="q":
        break
    elif mode=="view":
        view()
    else:
        add()
        continue
    
        
    
    
        
        
    


            
        
    