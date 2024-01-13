from apps.celery.utils import celery_apply_async
from apps.email.consts import EmailType
from apps.email.tasks import send_email_async
from config import settings

celery_apply_async(
    send_email_async,
    args=[
        EmailType.USER_REGISTER_EMAIL.value,
        ["knbgjkkmk@gmail.com"],
        {"email": "knbgjkkmk@gmail.com", "domain": settings.DOMAIN, "token_id": 123123123, "user_id": 456456456},
    ],
    countdown=1,
)
