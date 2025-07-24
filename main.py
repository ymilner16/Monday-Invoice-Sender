import crawler, os, requests
from dotenv import load_dotenv

#load .env file and initialize variables
load_dotenv()
URL = os.getenv('URL')
EMAIL = os.getenv('EMAIL')
PASS = os.getenv('PASS')

#call webcrawler and
crawler.login(URL, EMAIL, PASS)
invoice_URL = crawler.getInvoiceURL()
response = requests.get(invoice_URL)
print(invoice_URL)
with open('/tmp/Monday_Invoice.pdf', 'wb') as f:
    f.write(response.content)
