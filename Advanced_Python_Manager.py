from cryptography.fernet import Fernet
import hashlib
import os
def generate_key():
    key=Fernet.generate_key()#generate secure random key
    with open("master.key","wb")as f:
        f.write(key)
def load_key():
    return open("master.key","rb").read()
if not os.path.exists("master.key"):
            generate_key()  
fer=Fernet(load_key())    
def set_master_password():
    master=(input("Set Master Password: "))
    hashed=hashlib.sha256(master.encode()).hexdigest()
    with open("master.hash","w")as f:
        f.write(hashed)
    print("Master Password Set Successfully") 
def verify_master_password():
    master=int(input("Enter a master password: "))
    hashed=hashlib.sha256(master.encode()).hexdigest()
    stored=open("master.hash").read()
    return hashed==stored
if not os.path.exists("master.hash"):
    set_master_password()
    
#Password Functions
def add():
    account=input("Enter Account name: ")
    passwd=input("Enter Password: ")
    encrypted=fer.encrypt(passwd.encode()).decode()
    with open("passwords.txt","a") as f:
        f.write(account+"|" + encrypted +"\n")
    print("Password Saved Securely")
def view():
    if not os.path.exists("passwords.txt"):
        print("No Password Stored ")
        return
    with open("passwords.txt","r")as f:
        for line in f:
            account,_=line.strip().split("|")
            print(f"{account} : ********")
def verify_password():
    acc=input("Enter Account Name ")
    user_input=input("Enter Password to Verify ")
    with open("passwords.txt","r")as f:
        for line in f :
            account,encrypted=line.strip().split("|")
            if account==acc:
                real=fer.decrypt(encrypted.encode()).decode()
                if user_input==real:
                    print("Password Correct")
                else:
                    print("Incorrect")
                    return print("Account not found")
while True:
    print("\n1.Add Password")
    print("\n2.View Password")
    print("\n3.Verify Password")
    print("\n4.Exit")
    choice=input("choose: ")
    if choice=="1":
        add()
    elif choice=="2":
        view()
    elif choice=="3":
        verify_password()
    elif choice=="4":
        break  
    else:
        print("Invalid")
        
                

    
    






