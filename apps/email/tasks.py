from typing import Any, Dict, List

from celery import shared_task

from apps.email.consts import EmailType
from apps.email.services import EmailServices


@shared_task()
def send_email_async(
    email_type: EmailType,
    recipients: List[str],
    context: Dict[str, Any],
) -> None:
    EmailServices.send_email(email_type=email_type, recipients=recipients, context=context)
