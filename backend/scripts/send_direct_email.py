import django
import sys
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'carebackend.settings'
sys.path.append(os.path.dirname(__file__) + '/..')
django.setup()
from django.core.mail import EmailMultiAlternatives
from django.core import mail

if len(sys.argv) < 4:
    print("Missing args: Format is ADDRESS SUBJECT FILE")
    exit()
to_address = sys.argv[1]
subject = sys.argv[2]
file = sys.argv[3]

with open(file, 'r') as f:
    body = f.read()

with mail.get_connection() as connection:
    message = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email="SavingChinatown Team <info@savingchinatown.org>",
        to=[to_address],
        bcc=['cuianthony1@gmail.com'],
        connection=connection,
    )
    message.send()
    print("Sent email to", to_address)