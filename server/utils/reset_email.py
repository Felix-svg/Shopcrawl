from flask_jwt_extended import create_access_token
from datetime import timedelta
from flask_mail import Message
from config import mail

def send_reset_email(user):
    expires = timedelta(hours=1)  # Correct import and usage of timedelta
    reset_token = create_access_token(identity=user.id, expires_delta=expires)
    reset_url = f"https://shopcrawl.vercel.app/reset-password?token={reset_token}"
    msg = Message('Password Reset Request', sender='noreply@example.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {reset_url}
    If you did not make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)

