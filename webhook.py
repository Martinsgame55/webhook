import requests

# Microsoft Teams webhook URL (nutné získat a nahradit vaší URL)
webhook_url = "https://ssinfis.webhook.office.com/webhookb2/98a9afb8-a60e-484e-8d91-7a10722df49c@1543f07f-30f9-407a-9eb5-8a7aec418fff/IncomingWebhook/57c79eadb6d346b3825ed125ccc25a7b/7daf95c0-cff0-4c84-8585-aa64c6183e21/V2O8FEqZG1EZ1ztfDqiaboVN1zJLm52gQisdxcJFI6PwQ1"

# Zpráva, kterou chcete odeslat
data = {
    "text": "Ahoj, toto je zpráva z mého programu!"
}

# Odeslání HTTP POST požadavku na webhook URL
response = requests.post(webhook_url, json=data)

# Kontrola odpovědi
if response.status_code == 200:
    print("Zpráva úspěšně odeslána.")
else:
    print(f"Chyba při odesílání: {response.status_code} - {response.text}")
