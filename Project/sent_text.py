from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "YOUR ACCOUNT_SID"
AUTH_TOKEN = "YOUR AUTH_TOKEN"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    body  = "My Python training",
    to    = "+",
    from_ = "+")

print( message.sid)
