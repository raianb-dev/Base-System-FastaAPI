# Importações necessárias
from sqlalchemy.orm import Session
from sqlalchemy import and_
from dbconnection.connection import get_db
from models.modelsClient import Resident
from models.modelsNotification import Email
import requests
import uuid
import base64

# URL e autorização para envio de e-mails
url = 'https://api.mailersend.com/v1/email'
authorization = {"Authorization": "Bearer mlsn.4dc2b21b4adaa8ce54a384e63877dbc9b0f2f1a9b6fa2eed2df02c0fc09ca126"}

# Função para enviar e-mail e salvar notificação na base de dados
def send_email(barcode: str, block: str, apto: str, clientId: str, image: str):
    try:
        db = next(get_db())  # Obter a instância do banco de dados
        # Obtém o e-mail do residente com base no client_id
        resident = db.query(Resident).filter(and_(
            Resident.client_id == clientId,
            Resident.apto == apto,
            Resident.block == block
        )).first()
        if resident:
            email = resident.email
        else:
            return "Resident not found"

        # Codificar a imagem em base64
     

        # Dados para o envio do e-mail
        data = {
            "from": {
                "email": "info@trial-0p7kx4xqk7mg9yjr.mlsender.net",
                "name": "Domínio"
            },
            "to": [
                {
                    "email": email
                }
            ],
            "subject": "SUA ENCOMENDA CHEGOU: Favor retirar na portaria",
            "text": "Greetings from the team, you got this message through MailerSend.",
            "html": f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Sua Encomenda Chegou!</title>
                    <style>
                        body {{
                            font-family: 'Arial', sans-serif;
                            background-color: #f9f9f9;
                            margin: 0;
                            padding: 0;
                            text-align: center;
                        }}
                        .container {{
                            max-width: 600px;
                            margin: 0 auto;
                            padding: 20px;
                        }}
                        .header {{
                            background-color: #23b05e;
                            color: #fff;
                            padding: 20px;
                            border-radius: 10px 10px 0 0;
                        }}
                        .header h1 {{
                            margin: 0;
                            font-size: 24px;
                        }}
                        .barcode {{
                            color: #333;
                            font-size: 18px;
                            font-weight: bold
                        }}
                        .content {{
                            background-color: #fff;
                            padding: 20px;
                            border-radius: 0 0 10px 10px;
                        }}
                        .content p {{
                            margin: 10px 0;
                            font-size: 16px;
                        }}
                        .button {{
                            display: inline-block;
                            background-color: #ff6600;
                            color: #fff;
                            text-decoration: none;
                            padding: 10px 20px;
                            border-radius: 5px;
                            transition: background-color 0.3s ease;
                        }}
                        .button:hover {{
                            background-color: #cc4d00;
                        }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="header">
                            <h1>Sua Encomenda Chegou!</h1>
                        </div>
                        <div class="content">
                            <p>Olá, {resident.fullname}</p>
                            <img src="{image}" alt="{image}">
                            <p>Temos o prazer de informar que sua encomenda chegou à nossa portaria. Por favor, faça a retirada o mais breve possível.</p>
                            <p>Código de Barras: <span class="barcode">{barcode}</span></p>
                            <p>Agradecemos por escolher nossa empresa para suas compras!</p>
                            <p>Atenciosamente,<br>A equipe da Empresa Dominio</p>
                        </div>
                    </div>
                </body>
                </html>
            """
            
        }
        

        # Envio do e-mail
        req = requests.post(url, json=data, headers=authorization)
        req.raise_for_status()  # Verifica se houve erro no envio do e-mail

        # Adiciona a notificação de e-mail à base de dados
        add_notification(db, apto, block, req.status_code)

        return f"Email sent successfully CODE: {req.status_code}"
    except requests.RequestException as e:
        return f"Error sending email: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    finally:
        db.close()  # Fechar a sessão do banco de dados

# Função para adicionar notificação de e-mail à base de dados
def add_notification(db: Session, apto: str, block: str, status: int):
    try:
        uuidOne = str(uuid.uuid4())
        add = Email(
            id=uuidOne,
            apto=apto,
            block=block,
            status=status
        )
        db.add(add)
        db.commit()
        return "Notification added successfully"
    except Exception as e:
        return f"Error adding notification: {str(e)}"
