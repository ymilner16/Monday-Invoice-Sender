# Monday Invoice to Teams Tool

This tool is used to send the latest monday.com invoice via Teams\
**This project is still a WIP, currently only saves your latest invoice to /tmp/Monday_Invoice.pdf**

## How to run
Currently, to run the tool you need to create a venv with all modules from the requirements.txt file.\
Then, you simply create a file named .env in the project's folder, and set the following variables:

```env file
EMAIL="your email here"
PASS="your monday.com password here"
URL="https://<yourcompany>.monday.com/admin/billing/invoices"
```
