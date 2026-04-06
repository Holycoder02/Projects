# WhatsApp Automation Messages

A Python script to send scheduled WhatsApp messages using the Twilio API.

## Features
- Send WhatsApp messages to any recipient with a valid phone number
- Schedule messages to be sent at a specific date and time
- User-friendly input prompts
- Error handling with detailed error messages

## Prerequisites

- Python 3.x installed
- Twilio account with WhatsApp API access
- Twilio credentials (Account SID and Auth Token)

## Installation

1. **Install Twilio library:**
   ```bash
   pip install twilio
   ```

2. **Get Twilio Credentials:**
   - Create a Twilio account at https://www.twilio.com
   - Get your Account SID and Auth Token from the Twilio Console
   - Enable WhatsApp messaging in your Twilio account

3. **Update credentials in the script:**
   - Replace `account_sid` and `auth_token` with your actual credentials
   - Update the `from_` number with your Twilio WhatsApp number

## Usage

Run the script:
```bash
python main.py
```

Follow the prompts:
1. **Enter the recipient name** - Name of the person receiving the message
2. **Enter WhatsApp number** - Phone number with country code (e.g., +916299538998)
3. **Enter the message** - The message content to send
4. **Enter the date** - Date in YYYY-MM-DD format (e.g., 2026-04-06)
5. **Enter the time** - Time in HH:MM 24-hour format (e.g., 20:29)

The script will:
- Verify the scheduled time is in the future
- Wait until the scheduled time
- Send the WhatsApp message automatically

## Example

```
Enter the recipient name = Raju
Enter the recipient Whatsapp number with country code (e.g, +12345) = +9112345
enter the message you want to send to Raju: Hello! This is an automated message
enter the date to send the message (YYYY-MM-DD): 2026-04-06
enter the time to send the message (HH:MM in 24hour format): 20:30
Message scheduled to be sent to Raju at 2026-04-06 20:30:00.
Message sent successfully! Message SID: SM123
```

## Error Handling

If an error occurs, the script will display the error message. Common errors:

- **Invalid credentials** - Check your Account SID and Auth Token
- **Invalid phone number** - Ensure the number includes the country code with a single `+`
- **Invalid sender number** - Verify your Twilio WhatsApp number is correct
- **WhatsApp not enabled** - Enable WhatsApp in your Twilio account settings
- **Past date/time** - Always enter a future date and time

## Important Notes

- The script uses `time.sleep()` to wait until the scheduled time. Keep the script running until the message is sent.
- Phone numbers must include the country code (e.g., +91 for India, +1 for USA)
- Time must be in 24-hour format (00:00 to 23:59)
- Your Twilio account must have sufficient credits to send messages

## Security Warning

⚠️ **Never commit your Twilio credentials to version control!** Store them in environment variables or a separate config file.

## License

This project is open source and available for personal use.
