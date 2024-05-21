import random


class PasswordGenerator:
    ASCII_START = 41
    ASCII_FINISH = 122

    def generate_password(self, length: int):
        password = ""
        for i in range(length):
            password += chr(random.randint(self.ASCII_START, self.ASCII_FINISH))
        return password


if __name__ == "__main__":
    gen = PasswordGenerator()
    password = gen.generate_password(length=8)
    print(password)
