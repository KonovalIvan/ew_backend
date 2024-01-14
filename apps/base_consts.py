from apps.base_enums import ChoosableEnum

bytes_mb = 0.00000095367432
bytes_kb = 0.0009765625


class WebType(ChoosableEnum):
    REGISTER_VIEW = "REGISTER_VIEW"


TEMPLATE_WEB_DATA = {
    "REGISTER_VIEW": "confirm_email_view.html",
}