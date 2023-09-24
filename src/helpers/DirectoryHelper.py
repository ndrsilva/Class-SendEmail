"""..."""
from os import listdir
from os import path


class DirectoryHelper:
    """..."""

    def __init__(self, dir_path: str) -> None:
        """..."""

        self._dir = dir_path

    def list_files_type(self, extension: str) -> list:
        """..."""

        list_all = self._list_files_all()
        list_files = [file for file in list_all
                      if file.lower().endswith(extension)]

        return list_files

    def _list_files_all(self) -> list:
        """..."""

        list_files = [path.join(self._dir, nome)
                      for nome in listdir(self._dir)]

        return list_files


# Test
# if __name__ == '__main__':
#     directory_helper = DirectoryHelper(r'.\src\helpers\temp\x')
#     print(directory_helper.list_files_type('txt'))


