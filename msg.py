from password import EMAIL, EMAIL_PASSWORD, SECOND_ADDRESS
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(name=None, email=None, phone=None, message=None):
    assunto = f"Subject: Contact from page"
    texto = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

    corpo = MIMEText(texto, 'plain', 'utf-8')

    corpo['From'] = EMAIL
    corpo['To'] = SECOND_ADDRESS
    corpo['Subject'] = Header(assunto, 'utf-8')

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=SECOND_ADDRESS,
            msg=corpo.as_string())