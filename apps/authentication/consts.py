from apps.base_enums import ChoosableEnum


class UserType(ChoosableEnum):
    CLIENT = "Client"
    DESIGNER = "Designer"
    WORKER = "Worker"
    BUILDING_MASTER = "Building master"
