import os
import django
from django.core.mail import send_mail
from django.conf import settings

import sys
# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

def test_email():
    print(f"Attempting to send email from: {settings.EMAIL_HOST_USER}")
    print(f"Using Password: {settings.EMAIL_HOST_PASSWORD[:2]}...{settings.EMAIL_HOST_PASSWORD[-2:]}")
    
    subject = "Task Manager Email Test"
    message = "This is a test email to verify SMTP configuration."
    recipient = "chiduralaswaraj@gmail.com"
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            fail_silently=False,
        )
        print("SUCCESS: Email sent successfully!")
    except Exception as e:
        print(f"ERROR: Failed to send email: {e}")

if __name__ == "__main__":
    test_email()
