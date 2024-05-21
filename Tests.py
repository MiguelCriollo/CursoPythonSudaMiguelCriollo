def get_file():
    with open('estudiantes.txt', 'r') as file:
        return file.readlines()


def limit_print(file: list, limit: int = None   , only: int = None):
    if only is None:
        return file[:limit]
    else:
        return file[only:only+1]


name = limit_print(file=get_file(), only=2)
print(name)