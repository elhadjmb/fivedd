import os.path


class File:
    def __init__(self, path="/"):
        self.path = r"{}".format(path)  # if Checker.path(path) else Exceptions.flag(type=Dictionary.Internal())
        self.file_name = os.path.basename(self.path)
        self.size = os.path.getsize(self.path)
        self.extension = os.path.splitext(self.path)[1]
        self.name = self.file_name.replace(self.extension, "")
