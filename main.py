#install required libraries
from twilio.rest import Client
from datetime import datetime,timedelta
import time

#twilio credentials
#account_sid='AC51a6a5b5a17395e8ace1198be7dd7915'
#auth_token='b86bcc53d9b9d969c0dea06d742af335' 

client=Client(account_sid,auth_token)

#send message define
def send_whatsapp_message(recipient_number,message_body):
    try:
        message=client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
    
        print(f'message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occured')

#user input 
name=input('Enter the recipient name= ')
recipient_number=input('Enter the recipient Whatsapp number with country code (e.g, +12345)')
message_body=input(f'Enter the message you want to send to {name}:')

#parse date/time and calculate delay
date_str=input('Enter the date to send the message (YYYY-MM-DD)')
time_str=input('Enter the time to send the message (HH:MM in 24 hour format):')

#datetime module 
schedule_datetime=datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime=datetime.now()

#calculate delay
time_difference=schedule_datetime - current_datetime
delay_seconds=time_difference.total_seconds()

if delay_seconds <=0:
    print('The specified time is in the past. Please enter the future date and time:')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

    #wait for message 
    time.sleep(delay_seconds)

    #send message 
    send_whatsapp_message(recipient_number,message_body)
