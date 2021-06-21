import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from email.mime.base import MIMEBase
from email import encoders
from selenium.webdriver.chrome.options import Options


data_atual = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())#apenas um encremento para enviar a data junto ao corpo do email

dia_atual = (data_atual[:11]) 
hora_atual = (data_atual[11:]) 
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
email_from = '@gmail.com' #email que vai enviar
email_password = 'senha' #senha do emmail que vai enviar
email_sever = 'smtp.gmail.com'
destinacion = ['@gmail.com'] #email que vai receber

subject = 'test - Email Python'#esse é o titulo do email
msg = MIMEMultipart()
msg['From'] = email_from
msg['Subject'] = subject

text = f'''
<p>Planilha dinâmica Magazine Luiza</p>
<p>Data do envio: </p>
<p>Dia: {dia_atual}</p>
<p>Hora: {hora_atual}</p>
'''
#aqui em cima voce edita o corpo do email


msg_text  = MIMEText(text, 'html')
msg.attach(msg_text)


#Abrimos o arquivo em modo leitura e binary 
cam_arquivo = "C:\\Users\\user\\Downloads\\RESULTADO_1T21_POR.xlsx"#aqui voce passa o diretorio do arquivo que deseja enviar
attchment = open(cam_arquivo,'rb')

#Lemos o arquivo no modo binario e jogamos codificado em base 64 (que é o qual o e-mail precisa )
att = MIMEBase('application', 'octet-stream')
att.set_payload(attchment.read())
encoders.encode_base64(att)

#ADCIONAMOS o cabeçalho no tipo anexo de email 
att.add_header('Content-Disposition', f'attachment; filename=RESULTADO_1T21_POR.xlsx')
#fechamos o arquivo 
attchment.close()
msg.attach(att)
try:
    smtp = smtplib.SMTP(email_sever, 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email_from, email_password)
    smtp.sendmail(email_from, ','.join(destinacion), msg.as_string())
    smtp.quit()
    print("email enviado com sucesso")
except Exception as err:
    print(f'Falha ao enviar email: {err}')