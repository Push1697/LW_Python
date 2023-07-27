import smtplib  # Library used for mail
import ssl  # ssl for creating or established a Secure connection


def mail(sender_email, sender_password, receiver_email, subject, message):
    smtp_server = "smtp.gmail.com"
    port = 587

    context = ssl.create_default_context()  # Create the SSL/TLS connection

    server = smtplib.SMTP(smtp_server, port)
    server.starttls(context=context)  # Upgrade the connection to secure TLS

    # Login to the SMTP server with your email credentials
    server.login(sender_email, sender_password)

    # Compose the email
    email_message = (
        f"From: {sender_email}\nTo: {receiver_email}\nSubject: {subject}\n\n{message}"
    )

    # Send the email
    server.sendmail(sender_email, receiver_email, email_message)

    server.quit()


sender_email = "pushpendra.test45@gmail.com"
sender_password = "rblohtajsgkkqscj"
receiver_email = "push1697@gmail.com"
subject = "Meeting to be created"
message = "Hello, we will do this tomorrow"

mail(sender_email, sender_password, receiver_email, subject, message)
