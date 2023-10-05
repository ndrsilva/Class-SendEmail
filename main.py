"""..."""
import os
import json
from dotenv import load_dotenv
from src.helpers.DirectoryHelper import DirectoryHelper
from SendEmail import SendEmail
from message import message


def main():
    """..."""

    load_dotenv()
    dir_helper = DirectoryHelper(
        dir_path=os.getenv('DIR_FILES')
    )

    email = SendEmail()
    connection = email.configure_connection(
        smtp_server=json.loads(os.getenv('SERVER'))['gmail'],
        port=int(os.getenv('PORT')),
        sender_email=json.loads(os.getenv('SENDER_EMAIL'))['gmail'],
        password=json.loads(os.getenv('PASSWORD'))['gmail']
    )

    if connection:
        head = email.configure_head(
            sender_name=os.getenv('SENDER_NAME'),
            send_to=json.loads(os.getenv('SEND_TO'))['emails'],
            send_cc=json.loads(os.getenv('SEND_CC'))['emails'],
            subject=os.getenv('SUBJECT')
        )

        if head:
            message_true = email.attach_message(
                message=message
            )

            if message_true:
                file_true = email.attach_files(
                    list_files_paths=dir_helper.list_files_type(
                        extension='txt'
                    )
                )

                if file_true:
                    email.send()


if __name__ == '__main__':
    main()
