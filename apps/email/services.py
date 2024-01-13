from typing import Any, Dict, List

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from apps.authentication.models import User
from apps.authentication.selectors import UserSelector
from apps.email.consts import EMAIL_DATA, TEMPLATE_FOLDER, EmailType
from config import settings


class EmailServices:
    @staticmethod
    def send_email(
        email_type: EmailType,
        context: Dict[str, Any],
        recipients: List[str],
    ) -> None:
        _email_data = EMAIL_DATA[email_type]

        for recipient in recipients:
            user: User = UserSelector.get_by_username(recipient)
            _email_subject = _email_data["subject"][user.language]
            _html_name = f"{user.language}/{_email_data['html_template']}"

            html = render_to_string(f"{TEMPLATE_FOLDER}/{_html_name}", context)
            email = EmailMultiAlternatives(
                subject=_email_subject,
                alternatives=[(html, "text/html")],
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[recipient],
            )
            email.send()
