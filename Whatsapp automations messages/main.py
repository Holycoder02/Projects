"""
twilio 
date and time
time module

1- twilio client setup
2- user inputs
3- scheduling logic
4- send message


"""
# step 1 install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# step 2 twilio credentials
account_sid = 'AC8d01fcd0e6988b41daddb96ceed2f3f7'
auth_token = 'e740768d8e680711eda32b3a93ec4599'

client = Client(account_sid, auth_token)

#step 3 user inputs define send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'An error occurred: {e}')

#step 4 user input
name = input('Enter the recipient name = ')
recipient_number = input('Enter the recipient Whatsapp number with country code (e.g, +12345)')
message_body = input(f'enter the message you want to send to {name}: ')

#step 5 parse date/time and calculate delay
date_str = input('enter the date to send the message (YYYY-MM-DD): ')
time_str = input('enter the time to send the message (HH:MM in 24hour format): ')

#datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()


# calculate delay 
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past, Please enter a future date and time: ')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

    # wait until the scheduled time
    time.sleep(delay_seconds)     # this will pause the program until the specified time is reached
    send_whatsapp_message(recipient_number, message_body)


