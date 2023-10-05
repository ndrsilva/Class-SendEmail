"""..."""
import socket
import smtplib

from typing import Union

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

import logging as logger


class SendEmail:
    """..."""

    def __init__(self) -> None:
        """..."""

        logger.basicConfig(
            level=logger.INFO,
            format='%(asctime)s:-:%(name)s:-'
                   ':%(levelname)s:-:%(lineno)s:-:%(message)s',
            handlers=[logger.FileHandler('logger.txt', 'a'),
                      logger.StreamHandler()]
        )

        self.log = logger.getLogger(__name__)
        self._msg = None
        self._to_cc = None
        self._smtp = None

    def configure_connection(self, smtp_server: str, port: int, sender_email: str, password: str) -> bool:
        """..."""

        if self._check_internet_connection():
            self.log.info(
                'Internet connection ok.'
            )

            if not self._check_active_smtp(smtp_server, port):
                self.log.error(
                    f'The {smtp_server} server is not accessible'
                )
                return False

            self.log.info(
                f'The {smtp_server} server is accessible'
            )

            try:
                self._smtp = smtplib.SMTP(smtp_server, port)
                self._smtp.starttls()

                status_code, _ = self._smtp.login(
                    sender_email, password
                )

                if status_code == 235:
                    self.log.info(
                        f'Successfully authenticated to the {smtp_server}'
                    )
                    return True

            except Exception as exc:
                self.log.error(
                    f'Authentication failure with {smtp_server}.\nError: {exc}'
                )
                return False

        else:
            self.log.error(
                'Internet connection error.'
            )
            return False

    def _check_internet_connection(self) -> bool:
        """..."""

        try:
            socket.gethostbyname("www.google.com")

            self.log.debug('active internet')
            return True

        except socket.gaierror:

            self.log.debug(
                f'Internet inactive.'
            )
            return False

        except Exception as exc:

            self.log.debug(
                f'Internet inactive.\nError: {exc}'
            )
            return False

    def _check_active_smtp(self, smtp_server: str, port: int, timeout: int = 5) -> bool:
        """..."""

        try:
            sockett = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM
            )

            sockett.settimeout(timeout)
            sockett.connect((smtp_server, port))

            sockett.close()

            self.log.debug(
                'Active smtp gmail'
            )
            return True
        
        except Exception as exc:

            self.log.debug(
                f'SMTP Gmail inactive.\nError: {exc}'
            )
            return False

    def configure_head(self, sender_name: str, send_to: list, send_cc: list, subject: str) -> bool:
        """..."""

        try:
            self._to_cc = send_to + send_cc if send_cc is not None else send_to

            self._msg = MIMEMultipart()
            self._msg['From'] = Header(
                sender_name, 'utf-8'
            ).encode()
            self._msg['To'] = ','.join(send_to)
            self._msg['Cc'] = ','.join(send_cc)
            self._msg['Subject'] = subject

            self.log.info(
                'Success configuring the email header'
            )
            return True

        except Exception as exc:
            self.log.error(
                f'Error when configuring email header.\nError: {exc}'
            )
            return False

    def attach_message(self, message: str) -> bool:
        """..."""

        try:
            self._msg.attach(MIMEText(
                message, 'plain')
            )

            self.log.info(
                'Message attached successfully'
            )
            return True

        except Exception as exc:
            self.log.error(
                f'Error attaching message.\nError: {exc}'
            )
            return False

    def attach_files(self, list_files_paths: list) -> bool:
        """..."""

        try:
            for file_path in list_files_paths:

                file_name = self._get_file_name(file_path)

                if file_name is None:
                    return False

                with open(file_path, "r", encoding='utf-8') as file:
                    file_content = file.read()

                part = MIMEBase('application', "octet-stream")
                part.set_payload(file_content)

                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={Header(file_name, "utf-8").encode()}'
                )

                self._msg.attach(part)

            if list_files_paths:
                self.log.info('Success in attaching files')
            return True

        except Exception as exc:
            self.log.error(
                f'Error when attaching files.\nError: {exc}'
            )
            return False

    def _get_file_name(self, file_path: str) -> Union[str, None]:
        """..."""

        try:
            file_name = file_path.split('\\')

            self.log.debug(
                f'Successfully extracted file name: {file_name[-1]}'
            )
            return file_name[-1]

        except Exception as exc:
            self.log.debug(
                f'Error when trying to extract the file name.\nError: {exc}'
            )
            return None

    def send(self) -> None:
        """..."""

        try:
            self.log.info('Sending...')

            self._smtp.sendmail(
                self._msg['From'],
                self._to_cc,
                self._msg.as_string().encode('utf-8')
            )

            self.log.info('Sent...')
            self._smtp.quit()

        except Exception as exc:
            self.log.error(
                f'Error when trying to send the email.\nError: {exc}'
            )
