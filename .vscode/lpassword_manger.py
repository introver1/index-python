from cryptography.fernet import Fernet


# def write_key():
#     key = Fernet.generate_key()
#     with open("ket.key", "wb") as key_file:
#         key_file.write(key)

# write_key()   

def load_key():     
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



master_pwd = input("Enter your master password ")
key = load_key() + master_pwd.bytes
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f :
        for line in f.readlines():
            data = line.rstrip()
            user, passwd = data.split("|")
            print("User: ", user,  "," , "Password: ", passwd)
def add():
    name = input("Account name: ")
    pswd = input("Password: ")
    with open('passwords.txt', 'a') as f :
        f.write(name + "|" + str(fer.encrypt(pswd.encode())) + "\n")
        


while True:
    mode = input("Would you like to add a new password. If you want to add type 'add', to view type 'view' and to quit type 'quit'. ").lower()
    if mode == "quit":
        break
    if mode == "view":
        view()
    if mode == "add":
        add()
