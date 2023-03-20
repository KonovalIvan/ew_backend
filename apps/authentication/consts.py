from apps.base_enums import ChoosableEnum

DEFAULT_USER_LANGUAGE = "EN"


class UserType(ChoosableEnum):
    CLIENT = "Client"
    DESIGNER = "Designer"
    WORKER = "Worker"
    BUILDING_MASTER = "Building master"


class Language(ChoosableEnum):
    PL = "PL"
    EN = "EN"
    UA = "UA"
