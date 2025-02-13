import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587  # Use 465 for SSL
sender_email = 'aswin0526as@gmail.com'
sender_password = 'cnuzmutckmrlbmgu'
receiver_email = 'sec23cs156@sairamtap.edu.in'

# Create the email content
subject = 'Test Email'
body = 'This is a test email sent from Python.'

# Create a multipart message and set headers
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the body with the msg instance
message.attach(MIMEText(body, 'plain'))

try:
    # Connect to the server and log in
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Terminate the SMTP session and close the connection
    server.quit()
