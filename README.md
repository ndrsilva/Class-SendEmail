# Class SendEmail / Classe EnviarEmail
    - The objective of this class is to send a message with text files attached to its body,to an email
    list and copy to specific people.
    - Objetivo desta classe é enviar uma mensagem com arquivos de textos anexado ao seu corpo, para uma 
    lista de emails e copia as pessoas específicadas.


## Prerequisite / Pré-requisito:
- Python 3.8.3

## Requirements / Requerimentos
- certifi==2023.7.22
- charset-normalizer==3.2.0
- idna==3.4
- python-dotenv==1.0.0
- requests==2.31.0
- urllib3==2.0.5

## File message.py 
    - The message.py file has a constant so you can insert an email message.
    - No arquivo message.py tem uma constante para você poder inserir uma mensagem do email.

## Data that is in the .env file. <br> Dados que estão no arquivo .env
    - The data below is loaded into main.py, just create a .env file in 
    the project file and fill it with your data correctly in the structure below.
    - Os dados abaixo são carregados no main.py, basta criar um arquivo .env na
    raiz do projeto e prencher-lo com os seus dados corretamente na estrutura abaixo.

## .env file
    DIR_FILES = '.C:\Users\admin\Documents\files'
    
    SENDER_EMAIL = '{
                        "gmail": "sender@gmail.com",
                        "outlook": "sender@outlook.com"
                    }'
    
    PASSWORD = '{
                    "gmail": "password for Gmail app",
                    "outlook": "password for outlook app"
                }'
    
    SERVER = '{
                    "gmail": "smtp.gmail.com",
                    "outlook": "smtp-mail.outlook.com"
             }'
    
    PORT = 587
    
    SENDER_NAME = 'André Silva'
    
    SEND_TO = '{
                    "emails":[
                        "luan@gmail.com",
                        "julia@outlook.com.br"
                    ]
               }'
    
    SEND_CC = '{
                    "emails":[
                        "andre@gmail.com",
                        "luis@outlook.com.br"
    
                    ]
               }'
    
    SUBJECT = 'Email subject'

# Observation / Observação
    A Gmail email were used to send the emails with the SendEmail class, the password
    common will not work in this code, so you will need to generate a password for the app in the
    your gmail account settings. At the moment it only works with the Gmail account.

    Foi utilizado um email do gmail para enviar os emails com a class SendEmail, a senha 
    comum não irá funcionar nesse código, por isso será necessário gerar uma senha para app nas
    configurações da sua conta do gmail. No momento só funciona com a conta do Gmail.
