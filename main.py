import requests
import smtplib 
import email.message

# Pegar cotação do dólar - awesome API
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])

# Enviar o alerta - email
def enviar_email(cotacao_atual):  
    corpo_email = f"""
    <p>Dólar abaixo de R$5.20! Cotação atual: R${cotacao_atual}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Dólar hoje abaixo de 5.20"
    msg['From'] = 'remetente@gmail.com' # Alterar email
    msg['To'] = 'destinatario@gmail.com' # Alterar email
    password = 'vuwuzbnzuyqyuoaj' # Gerar nova senha no GMAIL em "senhas de app do google"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if cotacao < 5.20:
    enviar_email(cotacao)

# deploy - heroku
