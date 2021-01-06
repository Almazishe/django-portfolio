from django.conf import settings
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .token import account_activation_token


def send_confirmation_email(request, user):
    ''' Send email to user after registrations to confirm account '''

    current_site = get_current_site(request)
    mail_subject = 'Activate your account on Montessori Kazakhstan.'
    message = render_to_string('accounts/email/activate.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    to_email = user.email
    print(to_email)

    send_mail(
        subject=mail_subject,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[to_email],
        message=message,
        fail_silently=True,
    )

    print(to_email)





