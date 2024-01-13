from apps.base_enums import ChoosableEnum

TEMPLATE_FOLDER = "emails"
OS_TEMPLATES_FOLDER = "emails/"


class EmailType(ChoosableEnum):
    USER_REGISTER_EMAIL = "USER_REGISTER_EMAIL"


EMAIL_DATA = {
    "USER_REGISTER_EMAIL": {
        "html_template": "register_email.html",
        "subject": {
            "PL": "Rejestracja użytkownika",
            "EN": "User registration",
        },
    },
}
