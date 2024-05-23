import zipfile

zfile = zipfile.ZipFile('data.zip')
file = open('passwords.txt')

for password in file.readlines():
    try:
        zfile.extractall(pwd=password.encode('utf-8'))
        print("Password extracted successfully: ",password)
        break
    except RuntimeError as e:
        print("Wrong Password: ",password)
        continue
    except Exception as e:
        print("Unknown Error: ",password)
        continue