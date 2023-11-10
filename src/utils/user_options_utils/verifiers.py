import re
from typing import List, Tuple, Dict, Any, Optional

USERNAME = str
ROLES = List[str]
PASSWORD = str | None
PASSWORD_HASH = str | None
FULL_NAME = str | None
EMAIL = str | None
METADATA = Dict[str, Any] | None
ENABLED = bool

UserData = Tuple[USERNAME, ROLES, PASSWORD, PASSWORD_HASH, FULL_NAME, EMAIL, METADATA, ENABLED]


def verify(value: Optional[str]) -> bool:
    """
    Verify the value

    :param value:  String value
    :return:  Boolean True if valid, False if invalid
    """
    if value:
        return True
    return False


def verify_roles_regex_pattern(roles: str) -> bool:
    """
    Verify the roles regex pattern

    :return:  Boolean True if valid, False if invalid
    """
    pattern = r'^[a-zA-Z0-9_-]+(,[a-zA-Z0-9_-]+)*$'
    if re.match(pattern, roles):
        return True
    return False


def verify_password_length(password: PASSWORD) -> bool:
    """
    Verify the password length

    :param password:  String password
    :return:  Boolean True if valid, False if invalid
    """
    if len(password) >= 6:
        return True
    return False


def verify_if_space_exists_near_comma(value: str) -> bool:
    """
    Verify if the space exists after a comma in disabled features

    :param value:  String value
    :return:  Boolean True if valid, False if invalid
    """
    if re.search(r',\s', value) or re.search(r'\s,', value):
        return True
    return False


def verify_if_string_starts_with_comma(value: str) -> bool:
    """
    Verify if the string starts with a comma

    :param value:  String value
    :return:  Boolean True if valid, False if invalid
    """
    if value.startswith(','):
        return True
    return False


def verify_if_string_ends_with_comma(value: str) -> bool:
    """
    Verify if the string ends with a comma

    :param value:  String value
    :return:  Boolean True if valid, False if invalid
    """
    if value.endswith(','):
        return True
    return False


def verify_metadata_regex_pattern(metadata: str) -> bool:
    """
    Verify the metadata regex pattern

    :param metadata:  String metadata
    :return:  Boolean True if valid, False if invalid
    """
    pattern = r'^[a-zA-Z0-9_-]+:[a-zA-Z0-9_-]+(,[a-zA-Z0-9_-]+:[a-zA-Z0-9_-]+)*$'
    if re.match(pattern, metadata):
        return True
    return False


def verify_enabled_regex_pattern(enabled: str) -> bool:
    """
    Verify the enabled regex pattern

    :param enabled:  String enabled
    :return:  Boolean True if valid, False if invalid
    """
    pattern = r'^(true|false)$'
    if re.match(pattern, enabled):
        return True
    return False
