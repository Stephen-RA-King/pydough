#!/usr/bin/env python3
"""Facade script for email.message package."""

# Core Library modules
import mimetypes
import re
import smtplib
from email.message import EmailMessage
from pathlib import Path


class SendEmail:
    """Class to configure and store message and SMTP details and send email."""

    def __init__(
        self,
        user_id=None,
        user_pass=None,
        smtp_server=None,
        smtp_port=None,
        smtp_encryption="yes",
        smtp_authentication="yes",
    ):
        """Initialize class with set and default arguments."""
        self._user_id = user_id
        self._user_pass = user_pass
        self._display_password = None
        self._display_id = None
        self._smtp_server = smtp_server
        self._smtp_port = smtp_port
        self._smtp_encryption = smtp_encryption
        self._smtp_authentication = smtp_authentication
        self._test_sender = None
        self._test_recipient = None
        self._subject = None
        self._sender = None
        self._recipient = None
        self._cc = None
        self._validated_cc = None
        self._bcc = None
        self._validated_bcc = None
        self._body = None
        self._attachments = None
        self._msg_test = EmailMessage()
        self._msg = EmailMessage()

    @staticmethod
    def _validate_email(email):
        """Utility private method to validate email syntax."""
        _email_pattern = (
            r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:"
            r"[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
        )
        if isinstance(email, str) and re.search(_email_pattern, email):
            return True
        else:
            print(f"email '{email}', is not properly formatted")
            return False

    def _attach(self, file):
        filename = file.name
        ctype, encoding = mimetypes.guess_type(file)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)
        with open(file, "rb") as fp:
            self._msg.add_attachment(
                fp.read(), maintype=maintype, subtype=subtype, filename=filename
            )

    def __repr__(self):
        """Return detailed information about message and SMTP."""
        if self._user_id:
            self._display_id = "************ (Configured)"
        else:
            self._display_id = None
        return f"""
            {self.__class__.__name__},
            User ID: {self._display_id!r},
            Server:  {self._smtp_server!r},
            Port:    {self._smtp_port},
            SUBJECT: {self._subject},
            FROM:    {self._sender},
            TO:      {self._recipient},
            CC:      {self._validated_cc},
            BCC:     {self._validated_bcc},
            BODY:    {self._body}
        """

    def smtp_set(
        self,
        user_id=None,
        user_pass=None,
        smtp_server=None,
        smtp_port=None,
        smtp_encryption="yes",
        smtp_authentication="yes",
    ):
        """Sets and stores detailed SMTP information."""
        if user_id:
            self._user_id = user_id
        if user_pass:
            self._user_pass = user_pass
        if smtp_server:
            self._smtp_server = smtp_server
        if smtp_port:
            self._smtp_port = smtp_port
        if smtp_encryption:
            self._smtp_encryption = smtp_encryption
        if smtp_authentication:
            self._smtp_authentication = smtp_authentication

    def smtp_get(self):
        """Gets all SMTP Attributes."""
        if self._user_pass:
            self._display_password = "************ (Configured)"
        else:
            self._display_password = None
        if self._user_id:
            self._display_id = "************ (Configured)"
        else:
            self._display_id = None
        return f"""
            User ID:             {self._display_id},
            User Password:       {self._display_password},
            SMTP Server:(*)      {self._smtp_server},
            SMTP Port:(*)        {self._smtp_port},
            SMTP Encryption:     {self._smtp_encryption}
            SMTP Authentication: {self._smtp_authentication}
            * = Required
            """

    def smtp_test(self, sender, recipient):
        """Send a test message using configured SMTP settings."""
        self._msg_test = EmailMessage()
        if self._validate_email(sender):
            self._test_sender = sender
        else:
            return
        if self._validate_email(recipient):
            self._test_recipient = recipient
        else:
            return
        self._msg_test["Subject"] = "----- TEST MESSAGE -----"
        self._msg_test["From"] = self._test_sender
        self._msg_test["To"] = self._test_recipient
        self._msg_test["CC"] = []
        self._msg_test["BCC"] = []
        self._msg_test.set_content(
            "This is a test message......Your SMTP settings are correct!"
        )
        self._message_transmit(self._msg)

    def message_send(
        self,
        subject=None,
        sender=None,
        recipient=None,
        cc=None,
        bcc=None,
        body=None,
        attachments=None,
    ):
        """Will send the configured message using the configured SMTP settings."""
        self._validated_cc = []
        self._validated_bcc = []
        if subject:
            self._subject = subject
        if sender and self._validate_email(sender):
            self._sender = sender
        else:
            return
        if recipient and self._validate_email(recipient):
            self._recipient = recipient
        else:
            return
        if cc:
            self._cc = cc
            for i in self._cc:
                if self._validate_email(i):
                    self._validated_cc.append(i)
        if bcc:
            self._bcc = bcc
            for i in self._bcc:
                if self._validate_email(i):
                    self._validated_bcc.append(i)
        if body:
            self._body = body
        self._msg["Subject"] = self._subject
        self._msg["From"] = self._sender
        self._msg["To"] = self._recipient
        self._msg["CC"] = self._validated_cc
        self._msg["BCC"] = self._validated_bcc
        self._msg.set_content(self._body)
        if attachments:
            self._attachments = attachments
            for file in self._attachments:
                file = Path(file)
                if file.exists():
                    self._attach(file)
                continue
        self._message_transmit(self._msg)

    def message_get(self):
        """Get the message settings which are currently set."""
        return f"""
            c = Compulsory
            SUBJECT:(c) {self._subject },
            FROM:(c)    {self._sender},
            TO:(c)      {self._recipient},
            CC:         {self._validated_cc},
            BCC:        {self._validated_bcc},
            BODY:       {self._body}
        """

    def message_clear(self):
        """Clears the message settings."""
        if self._msg:
            self._msg.clear()

    def _message_transmit(self, message):
        """Connect to the SMTP server and send the message."""
        if not self._smtp_server or not self._smtp_port:
            print("Some SMTP server details are missing")
            print(self.smtp_get())
            return
        if not self._msg["Subject"] or not self._msg["From"] or not self._msg["To"]:
            print("Some Message details are missing")
            print(self.message_get())
            return

        with smtplib.SMTP(self._smtp_server, self._smtp_port) as server:
            if self._smtp_encryption == "yes":
                server.starttls()
            if self._smtp_authentication == "yes":
                server.login(self._user_id, self._user_pass)
            try:
                server.send_message(message)
            except smtplib.SMTPResponseException as e:
                error_code = str(e.smtp_code)
                error_message = str(e.smtp_error)
                print(f"Error Code: {error_code}:  {error_message}")
