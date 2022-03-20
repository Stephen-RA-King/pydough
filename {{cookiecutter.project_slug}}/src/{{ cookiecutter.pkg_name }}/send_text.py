#!/usr/bin/env python3
"""Utility script demonstrating the use of the send_email.py script."""

# Core Library modules
import configparser

# Third party modules
import keyring
import send_email

# Get SMTP Settings from Config file and Credentials from Keyring
service = "gmail"
ini = configparser.ConfigParser()
ini.read("email_config.ini")
server = ini.get(service, "smtp_server")
port = int(ini.get(service, "smtp_port"))
auth = ini.get(service, "smtp_authentication")
encrypt = ini.get(service, "smtp_encryption")
if auth == "yes":
    user_id = keyring.get_password(service, "service_id")
    user_pass = keyring.get_password(service, "service_password")
    if user_id is None or user_pass is None:
        raise NameError("Email ID or Password do not exist in Keyring")
else:
    user_id, user_pass = None, None


# STEP 1 - Configure SMTP ##################
mailer = send_email.SendEmail(
    user_id=user_id,
    user_pass=user_pass,
    smtp_server=server,
    smtp_port=port,
    smtp_authentication=auth,
    smtp_encryption=encrypt,
)

# STEP 2 - set message details #############
subject = "Title"
sender = user_id
recipient = ""
body = """Dear ... \n\nThis is a test"""
cc = [
    "user1@domain1.com",
]
bcc = [
    "user2@domain2.com",
]
attachments = ["attach1.jpg"]


# STEP 3 - Now send message ################
mailer.message_send(
    subject=subject,
    sender=sender,
    recipient=recipient,
    body=body,
    cc=cc,
    bcc=bcc,
    attachments=attachments,
)
