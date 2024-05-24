from cryptography.fernet import Fernet
import os

def retornarKey():
    return open("key.key", "rb").read()

def decryp(items, key):
    i = Fernet(key)
    for x in items:
        try:
            with open(x, "rb") as file:
                file_data = file.read()
            data = i.decrypt(file_data)
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
    
    # Eliminar el archivo readme.txt si existe
    readme_path = os.path.join(archivos, "readme.txt")
    if os.path.exists(readme_path):
        os.remove(readme_path)
    
    # Obtener todos los archivos en el directorio y subdirectorios
    archivos_2 = obtener_archivos_recursivamente(archivos)
    
    key = retornarKey()
    decryp(archivos_2, key)