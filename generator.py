class DirectoryGenerator:
    def __init__(self, base_path):
        self.base_path = base_path

    def create_file(self, path, content):
        with open(path, 'w') as file:
            file.write(content)