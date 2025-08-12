import msal, requests

def initialize(CLIENT, SECRET, TENANT):
    CLIENT_ID = CLIENT
    CLIENT_SECRET = SECRET
    TENANT_ID = TENANT
    AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
    SCOPES = ["Chat.ReadWrite", "User.Read", "Files.ReadWrite"]

    app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY)

    flow = app.initiate_device_flow(scopes=SCOPES)
    if "user_code" not in flow:
        raise Exception("Failed to initiate device flow")

    print(f"Go to {flow['verification_uri']} and enter code: {flow['user_code']}")
    result = app.acquire_token_by_device_flow(flow)

    if "access_token" not in result:
        raise Exception("Token acquisition failed")

    token = result["access_token"]
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

def sendFile(filePath, chatID):
    with open(filePath, "rb") as f:
        uploadResp = requests.put(
            f"https://graph.microsoft.com/v1.0/me/drive/root:/{FILENAME}:/content",
            headers={"Authorization": f"Bearer {token}", "Content-Type": "application/octet-stream"},
            data=f
    )

    if uploadResp.status_code not in (200, 201):
        raise Exception(f"Fule upload failed: {uploadResp.text}")

    fileInfo = uploadResp.json()
    fileURL = fileInfo.get("webUrl")

    message = {
        "body": {
        "contentType": "html",
        "content": f"Monday Invoice: <a href='{file_web_url}'>{FILENAME}</a>"
    }}
    messageResp = requests.post(
        f"https://graph.microsoft.com/v1.0/chats/{chat_id}/messages",
        headers=headers,
        json=message_payload
    )

    if messageResp.status_code in (200, 201):
        print("Message was sent with link")
