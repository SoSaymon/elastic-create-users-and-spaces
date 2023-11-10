import re
from typing import List, Tuple, Dict, Any, Callable
from .user_options_utils.verifiers import verify, verify_roles_regex_pattern, verify_password_length, \
    verify_if_space_exists_near_comma, verify_if_string_starts_with_comma, verify_if_string_ends_with_comma, \
    verify_metadata_regex_pattern, verify_enabled_regex_pattern
from .user_options_utils.utils import get_input

USERNAME = str
ROLES = List[str]
PASSWORD = str | None
PASSWORD_HASH = str | None
FULL_NAME = str | None
EMAIL = str | None
METADATA = Dict[str, Any] | None
ENABLED = bool

UserData = Tuple[USERNAME, ROLES, PASSWORD, PASSWORD_HASH, FULL_NAME, EMAIL, METADATA, ENABLED]


def get_and_verify_user_options() -> UserData:
    """
    Get and verify user options

    :return:  A tuple of user options.
    """
    username = get_and_verify_username()
    roles = get_and_verify_roles()
    password = get_and_verify_password()
    if password is None:
        password_hash = get_and_verify_password_hash()
    else:
        password_hash = None
    full_name = get_and_verify_full_name()
    email = get_and_verify_email()
    metadata = get_and_verify_metadata()
    enabled = get_and_verify_enabled()

    return username, roles, password, password_hash, full_name, email, metadata, enabled


def get_and_verify_username(get_user_username_fn: Callable[[str], str] = get_input) -> USERNAME:
    """
    Get and verify the username

    :return:  String username
    """
    while True:
        username = get_user_username_fn('Enter the username (Required): ')
        username = username.strip()

        if verify(username):
            return username
        print('Username is required.')


def get_and_verify_roles(get_user_role_fn: Callable[[str], str] = get_input) -> ROLES:
    """
    Get and verify the roles

    :return:  List of roles or None
    """
    while True:
        roles = get_user_role_fn('Enter the roles (Required, comma separated): ')
        roles = roles.strip()

        if verify(roles):

            if verify_if_space_exists_near_comma(roles):
                roles = roles.replace(', ', ',')
                roles = roles.replace(' ,', ',')

            if verify_roles_regex_pattern(roles):
                return roles.split(',')
            else:
                print('Roles must be comma separated. Example: role1,role2')

        else:
            print('Roles are required.')


def get_and_verify_password(get_user_password_fn: Callable[[str], str] = get_input) -> PASSWORD:
    """
    Get and verify the password

    :return:  String of password or None
    """
    while True:
        password = get_user_password_fn('Enter the password (Optional if you will use password_hash): ')
        password = password.strip()

        if verify(password):
            if verify_password_length(password):
                return password

            print('Password must be at least 6 characters.')
            continue

        return None


def get_and_verify_password_hash(get_user_password_hash_fn: Callable[[str], str] = get_input) -> PASSWORD_HASH:
    """
    Get and verify the password hash

    :return:  String of password hash
    """
    while True:
        password_hash = get_user_password_hash_fn('Enter the password hash (Required): ')
        password_hash = password_hash.strip()

        if verify(password_hash):
            return password_hash
        print('Password hash is required.')


def get_and_verify_full_name(get_user_full_name_fn: Callable[[str], str] = get_input) -> FULL_NAME:
    """
    Get and verify the full name

    :return:  String of full name or None
    """
    while True:
        full_name = get_user_full_name_fn('Enter the full name (Optional): ')
        full_name = full_name.strip()

        if verify(full_name):
            return full_name
        return None


def get_and_verify_email(get_user_email_fn: Callable[[str], str] = get_input) -> EMAIL:
    """
    Get and verify the email

    :return:  String of email or None
    """
    while True:
        email = get_user_email_fn('Enter the email (Optional): ')
        email = email.strip()

        if verify(email):
            return email
        return None


def get_and_verify_metadata(get_user_metadata_fn: Callable[[str], str] = get_input) -> METADATA:
    """
    Get and verify the metadata

    :return:  Dict of metadata or None
    """
    while True:
        metadata = get_user_metadata_fn('Enter the metadata (Optional, comma separated, key:value format): ')
        metadata = metadata.strip()

        if verify(metadata):

            if verify_if_space_exists_near_comma(metadata):
                metadata = metadata.replace(', ', ',')
                metadata = metadata.replace(' ,', ',')

            if verify_if_string_starts_with_comma(metadata):
                metadata = metadata[1:]

            if verify_if_string_ends_with_comma(metadata):
                metadata = metadata[:-1]

            if verify_metadata_regex_pattern(metadata):
                return dict(item.split(':') for item in metadata.split(','))
            else:
                print('Metadata must be comma separated and in key:value format. Example: key1:value1,key2:value2')
                print('If you do not want to set metadata, leave the field blank.')
                continue

        return None


def get_and_verify_enabled(get_user_enabled_fn: Callable[[str], str] = get_input) -> ENABLED:
    """
    Get and verify the enabled status

    :return:  True if enabled, False if disabled
    """
    while True:
        enabled = get_user_enabled_fn('Enter the enabled status (Optional (default: True), True/False): ')
        enabled = enabled.strip().lower()

        if verify(enabled):

            if verify_enabled_regex_pattern(enabled):
                return enabled == 'true'
            else:
                print('Enabled status must be either true or false.')
                print('If you do not want to set enabled status, leave the field blank.')
                continue

        return True
