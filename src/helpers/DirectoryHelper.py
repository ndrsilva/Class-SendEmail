"""..."""
import logging as logger

from os import listdir
from os import path
from typing import Union


class DirectoryHelper:
    """..."""

    def __init__(self, dir_path: str) -> None:
        """..."""

        logger.basicConfig(
            level=logger.INFO,
            format='%(asctime)s:-:%(name)s:-'
                   ':%(levelname)s:-:%(lineno)s:-:%(message)s',
            handlers=[logger.FileHandler('logger.txt', 'a'),
                      logger.StreamHandler()]
        )

        self.log = logger.getLogger(__name__)
        self._dir = dir_path

    def list_files_type(self, extension: str) -> Union[list, None]:
        """..."""

        try:
            list_all = [path.join(self._dir, nome)
                          for nome in listdir(self._dir)]

            list_files = [file for file in list_all
                          if file.lower().endswith(extension)]

            if len(list_files) == 0:
                self.log.info('No files to send.')
                return list_files

            self.log.debug(
                'File(s) listed successfully.'
            )
            return  list_files

        except Exception as exc:
            self.log.debug(
                f'Error listing files.\nError: {exc}'
            )
            return None


# Test
# if __name__ == '__main__':
#     directory_helper = DirectoryHelper(r'.\src\helpers\temp\x')
#     print(directory_helper.list_files_type('txt'))


