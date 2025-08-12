# Monday Invoice to Gmail Tool

This tool is used to send the latest monday.com invoice via Google Workspace (Gmail)

## How to run
Currently, to run the tool you need to create a venv with all modules from the requirements.txt file.\
Then, you simply create a file named .env in the project's folder, and set the following variables:

```env file
EMAIL="your email here"
PASS="your monday.com password here"
URL="https://<yourcompany>.monday.com/admin/billing/invoices"
RECIPIENT="the email you want to send the invoice to"
APP_PASS="your Google app password"
```
