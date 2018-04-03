from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb14941a78ae07ef8606633025e4df04a"
# Your Auth Token from twilio.com/console
auth_token  = "7373e693026ade6c73602592c629a728"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19704479505", 
    from_="+17089800107",
    body="On Sunday, the Catholic Church across the United States will celebrate the beginning of National Migration Week.")

print(message.sid)
