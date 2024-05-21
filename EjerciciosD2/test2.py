import os

search=['bd','sql','key','pem']
for dirpath, dirnames, filenames in os.walk(top='C:\\Users\\migue\\CursoPythonSuda\\CursoPythonSuda\\EjerciciosD2\\recursos'):
    for name in filenames:
        separeted_name=name.split('.')
        if separeted_name[-1] in search:
            print(os.path.join(dirpath, name))

if __name__ == '__main__':
    pass
