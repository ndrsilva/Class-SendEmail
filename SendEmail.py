"""..."""
import smtplib

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


class SendEmail:
    """..."""

    def __init__(self) -> None:
        """..."""

        self._msg = None
        self._to_cc = None
        self._smtp = None

    def configure_connection(self, server: str, port: int, sender_email: str, password: str) -> None:
        """..."""

        self._smtp = smtplib.SMTP(server, port)
        self._smtp.starttls()
        self._smtp.login(sender_email, password)

    def configure_head(self, sender_name: str, send_to: list, send_cc: list, subject: str) -> None:
        """..."""

        self._to_cc = send_to + send_cc if send_cc is not None else send_to

        self._msg = MIMEMultipart()
        self._msg['From'] = Header(sender_name, 'utf-8').encode()
        self._msg['To'] = ','.join(send_to)
        self._msg['Cc'] = ','.join(send_cc)
        self._msg['Subject'] = subject

    def attach_message(self, message: str) -> None:
        """..."""

        self._msg.attach(MIMEText(message))

    def attach_files(self, list_files_paths: list) -> None:
        """..."""

        for file_path in list_files_paths:
            
            file_name = self._get_file_name(file_path)

            with open(file_path, "r", encoding='utf-8') as file:
                file_content = file.read()

            part = MIMEBase('application', "octet-stream")
            part.set_payload(file_content)

            part.add_header(
                'Content-Disposition',
                f'attachment; filename={Header(file_name, "utf-8").encode()}'
            )

            self._msg.attach(part)

    @staticmethod
    def _get_file_name(file_path: str) -> str:
        """..."""

        file_name = file_path.split('\\')
        return file_name[-1]

    def send(self) -> None:
        """..."""

        self._smtp.sendmail(
            self._msg['From'],
            self._to_cc,
            self._msg.as_string().encode('utf-8')
        )

        print('Sent...')
        self._smtp.quit()

