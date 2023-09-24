# Class SendEmail / Classe EnviarEmail
    - The objective of this class is to send a message with text files attached to its body,to an email
    list and copy to specific people.
    - Objetivo desta classe é enviar uma mensagem com arquivos de textos anexado ao seu corpo, para uma 
    lista de emails e copia as pessoas específicadas.


## Prerequisite / Pré-requisito:
- Python 3.8.3


## Requirements:
- python-dotenv==1.0.0
  
        - Obs.: It is only necessary if you are going to use an environment variable with 
        the data in the .env file.
        - Só é necessário se for usar variável de ambiente com os dados no arquivo .env


## File message.py 
    - The message.py file has a constant so you can insert an email message.
    - No arquivo message.py tem uma constante para você poder inserir uma mensagem do email.

## Data that is in the .env file. <br> Dados que estão no arquivo .env
    - The data below is loaded into main.py, just create a .env file in 
    the project file and fill it with your data correctly.
    - Os dados abaixo são carregados no main.py, basta criar um arquivo .env na
    raiz do projeto e prencher-lo com os seus dados corretamente.

## .env file
    DIR_FILES = '.C:\Users\admin\Documents\files'
    
    SENDER_EMAIL = '{
                        "gmail": "sender@gmail.com",
                        "outlook": ""
                    }'
    
    PASSWORD = '{
                    "gmail": "password for Gmail app",
                    "outlook": ""
                }'
    
    SERVER = '{
                    "gmail": "smtp.gmail.com",
                    "outlook": "smtp.live.com"
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
                        "andregmail.com",
                        "luis@outlook.com.br"
    
                    ]
               }'
    
    SUBJECT = 'Email subject'

# Observation / Observação
    It was using a gmail email to be able to send the emails using the SendEmail class, the common
    password will not work in this code, so you will need to generate a password for the app in your
    gmail account settings.

    Foi usando um email do gmail para poder enviar os emails usando a class SendEmail, a senha 
    comum não irá funcionar nesse código, por isso será necessário gerar uma senha para app nas
    configurações da sua conta do gmail.
