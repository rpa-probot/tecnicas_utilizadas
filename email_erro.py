import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# ENVIANDO E-MAIL VIA SMTP, CONFIGURAÇÃO VIA MIME

# 1° Definimos o Remetente, a Senha (exclusiva para o bot, diferente da utilizada comumente) e o(s) Destinatário(s);
# 2° Configuramos o Assunto do e-mail, o Body e o seu conteúdo;
# 3° Inicializamos o Servidor SMTP e sua criptografia;
# 4° Enviamos o e-mail e encerramos o Servidor.

def nf_erro(numero_nfe):

    remetente = 'email_remetente@gmail.com'
    senha = '**********'
    destinatario = ('email_destinatario1@gmail.com,email_destinatario2@gmail.com,email_destinatario3@gmail.com')

    message = MIMEMultipart('related')
    message['From'] = remetente
    message['To'] = destinatario
    message['Subject'] = 'RPA - NOTA FISCAL'

    # CONTEÚDO ORIGINAL SENSÍVEL
    MIMEText(f'Nota Fiscal: {numero_nfe} COM ERRO!') # MENSAGEM GENÉRICA DO BODY DO E-MAIL

    session = smtplib.SMTP('protocolo_smtp.gmail.com', port=587)
    session.starttls()
    session.login(remetente, senha)
    text = message.as_string()

    session.sendmail(remetente, destinatario.split(","), text)
    session.quit()

    return True
