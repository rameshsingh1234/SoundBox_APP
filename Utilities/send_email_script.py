import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import configparser


def send_email(username, password, recipient_email):
    subject = "Selenium Test Execution Report"
    body = "Please find the attached test execution report."

    sender_email = username
    receiver_email = recipient_email

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Attach the test report file
    with open('reports/report.html', 'rb') as f:
        attach = MIMEApplication(f.read(), _subtype="html")
        attach.add_header('Content-Disposition', 'attachment', filename=str("report.html"))
        msg.attach(attach)

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.init')

    gmail_username = config['EMAIL']['username']
    gmail_password = config['EMAIL']['password']
    recipient_email = config['EMAIL']['recipient_email']

    subject = "Mobile automation Test Report"
    body = """
    Hi there,
    Here's the test report for the latest test run.
    Please find the attached report for more details.
    """

    send_email(gmail_username, gmail_password, recipient_email)
