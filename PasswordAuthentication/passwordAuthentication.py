import getpass

database = {"vietcuong104": "daitinh9x", "vlxx.tv": "anhsai"}
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Password incorrect! Re-enter your password: ")
        break

print("Verified!")
