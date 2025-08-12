import os
import smtplib
import ssl
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # TLS

def send_mail(pdf_path: str, sender: str, recipient: str, app_password: str) -> None:
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(pdf_path)

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = "Monday Invoice"
    msg.set_content("Attached: Monday invoice.")

    with open(pdf_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(pdf_path),
        )

    context = ssl.create_default_context()
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=30) as smtp:
        smtp.ehlo()
        smtp.starttls(context=context)
        smtp.ehlo()
        smtp.login(sender, app_password)
        smtp.send_message(msg)
RECIPIENT
