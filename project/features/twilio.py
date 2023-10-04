import os

from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
twilio_number = os.getenv('TWILIO_NUMBER')

class TwilioService:
    def __init__(self):
        pass # REST client is stateless, no need to instantiate anything
        
    def get_sender_wpp_number(self, form_data: dict) -> str:
        return form_data['From'].split("whatsapp:")[-1]
    
    def send_wpp_message(self, to_number, content):
        message = client.messages.create(
            from_=f"whatsapp:{twilio_number}",
            body=content,
            to=f"whatsapp:{to_number}"
            )
        
        return message