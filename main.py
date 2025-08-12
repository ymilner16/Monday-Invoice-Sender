import crawler, os, requests, gmail
from dotenv import load_dotenv

#load .env file and initialize variables
load_dotenv()
URL = os.getenv('URL')
EMAIL = os.getenv('EMAIL')
PASS = os.getenv('PASS')
APP_PASS = os.getenv('APP_PASS')
INVOICE_LOCAL = "/tmp/Monday_Invoice.pdf"
RECIPIENT = os.getenv('RECIPIENT')

#call webcrawler and download PDF
crawler.login(URL, EMAIL, PASS)
invoice_URL = crawler.getInvoiceURL()
response = requests.get(invoice_URL)
with open(INVOICE_LOCAL, 'wb') as f:
    f.write(response.content)

#send email with invoice attached
gmail.send_mail(INVOICE_LOCAL, EMAIL, EMAIL, APP_PASS)
