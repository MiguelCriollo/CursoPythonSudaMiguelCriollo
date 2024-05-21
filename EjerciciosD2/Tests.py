class FileManager:
    def __init__(self):
        self.filename = self.create_file()
        self.start_file_manager()

    @staticmethod
    def show_menu():
        print(f"""
            Fila Management Menu
            1. Select New File
            2. See all file data
            3. Add Collaborator
            4. Print Limited
            5. Exit        
        """)

    def start_file_manager(self):
        while True:
            prompt = self.menu_input()
            if prompt: break
        print("Program has ended")

    def menu_input(self):
        self.show_menu()
        while True:
            try:
                inputMenu = int(input("------>"))
            except Exception as e:
                print("Invalid input, try again")
                continue
            if inputMenu == 1:
                self.create_file()
            elif inputMenu == 2:
                self.print_data()
            elif inputMenu == 3:
                self.add_collaborator()
            elif inputMenu == 4:
                self.limit_print()
            return inputMenu == 5

    @staticmethod
    def create_file():
        while True:
            filename = input("Input the file name to manage:")
            try:
                open(filename, 'x')
                print("File doesn't exist, a new one has been created")
            except FileExistsError:
                print("File Exists!")
            finally:
                return filename

    def write_file(self, message: str):
        with open(self.filename, 'a') as file:
            file.write('\n' + message)

    def read_all_data(self):
        with open(self.filename, 'r') as file:
            return file.read().split('\n')

    @staticmethod
    def limit_data(file: list, limit, only: int = None):
        if limit is None: limit = 5
        limit=int(limit)
        if only is None:
            return file[:limit]
        else:
            return file[only:only + 1]

    def add_collaborator(self):
        data = self.read_all_data()
        if len(data) >= 15:
            print("Cannot add collaborator, max limit is 15")
        else:
            collaborator = input("Input the collaborator to add:")
            self.write_file(collaborator)

    def limit_print(self):
        data = self.read_all_data()
        limit = input("Input the limit to print: ")
        if limit == '': limit = None
        print(self.limit_data(file=data, limit=limit))

    def print_data(self):
        print(self.read_all_data())


if __name__ == '__main__':
    file_manager = FileManager()
