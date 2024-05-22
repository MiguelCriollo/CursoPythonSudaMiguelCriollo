import argparse
import os


search=['bd','sql','key','pem']
for dirpath, dirnames, filenames in os.walk(top='C:\\Users\\migue\\CursoPythonSuda\\CursoPythonSuda\\EjerciciosD2\\recursos'):
    for name in filenames:
        separeted_name=name.split('.')
        if separeted_name[-1] in search:
            print(os.path.join(dirpath, name))


parser = argparse.ArgumentParser(description="Sex2")
parser.add_argument('archivo', type=str, help='Nombre archivo')
parser.add_argument('--modo', choices=['lectura' , 'escritura'], default='lectura', help='MOdo Operaicon')
args = parser.parse_args()
print(f"Archivos: {args.archivo}")
print(f"Modo: {args.modo}")

if __name__ == '__main__':
    pass
