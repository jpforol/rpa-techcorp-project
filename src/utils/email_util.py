import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.config import EMAIL_SERVER, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD

def send_email(to_address, subject, body):
    """ Send an email with the provided subject and body """
    from_address = EMAIL_USER
    
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT)
    server.starttls()
    server.login(from_address, EMAIL_PASSWORD)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()

# Example usage
if __name__ == "__main__":
    send_email(
        to_address='test@example.com',
        subject='Test Email',
        body='This is a test email sent from our RPA system.'
    )
