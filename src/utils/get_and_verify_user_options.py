import re
from typing import List, Tuple, Dict, Any

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


def get_and_verify_username() -> USERNAME:
    """
    Get and verify the username
    :return:  String username
    """
    while True:
        username = input('Enter the username (Required): ')

        if username:
            username = username.strip()
            return username
        print('Username is required.')


def get_and_verify_roles() -> ROLES:
    """
    Get and verify the roles
    :return:  List of roles or None
    """
    while True:
        roles = input('Enter the roles (Required, comma separated): ')

        if roles:
            roles = roles.strip()
            pattern = r'^[a-zA-Z0-9_-]+(,[a-zA-Z0-9_-]+)*$'
            if re.match(pattern, roles):
                return roles.split(',')
            elif not re.match(pattern, roles):
                print('Roles must be comma separated. Example: role1,role2')
            else:
                print('Roles are required.')

        else:
            print('Roles are required.')


def get_and_verify_password() -> PASSWORD:
    """
    Get and verify the password
    :return:  String of password or None
    """
    while True:
        password = input('Enter the password (Optional if you will use password_hash): ')

        if password:
            password = password.strip()
            if len(password) <= 6:
                print('Password must be at least 6 characters.')
                continue
            return password

        return None


def get_and_verify_password_hash() -> PASSWORD_HASH:
    """
    Get and verify the password hash
    :return:  String of password hash
    """
    while True:
        password_hash = input('Enter the password hash (Required): ')

        if password_hash:
            password_hash = password_hash.strip()
            return password_hash
        print('Password hash is required.')


def get_and_verify_full_name() -> FULL_NAME:
    """
    Get and verify the full name
    :return:  String of full name or None
    """
    while True:
        full_name = input('Enter the full name (Optional): ')

        if full_name:
            full_name = full_name.strip()
            return full_name
        return None


def get_and_verify_email() -> EMAIL:
    """
    Get and verify the email
    :return:  String of email or None
    """
    while True:
        email = input('Enter the email (Optional): ')

        if email:
            email = email.strip()
            return email
        return None


def get_and_verify_metadata() -> METADATA:
    """
    Get and verify the metadata
    :return:  Dict of metadata or None
    """
    while True:
        metadata = input('Enter the metadata (Optional, comma separated, key:value format): ')
        if metadata:
            metadata = metadata.strip()

            if re.search(r',\s', metadata):
                metadata = metadata.replace(', ', ',')

            if re.search(r'\s,', metadata):
                metadata = metadata.replace(' ,', ',')

            if metadata.startswith(','):
                metadata = metadata[1:]

            if metadata.endswith(','):
                metadata = metadata[:-1]

            pattern = r'^[a-zA-Z0-9_-]+:[a-zA-Z0-9_-]+(,[a-zA-Z0-9_-]+:[a-zA-Z0-9_-]+)*$'
            if re.match(pattern, metadata):
                return dict(item.split(':') for item in metadata.split(','))
            elif not re.match(pattern, metadata) and metadata != '':
                print('Metadata must be comma separated and in key:value format. Example: key1:value1,key2:value2')
                print('If you do not want to set metadata, leave the field blank.')
                continue
        return None


def get_and_verify_enabled() -> ENABLED:
    """
    Get and verify the enabled status
    :return:  True if enabled, False if disabled
    """
    while True:
        enabled = input('Enter the enabled status (Optional (default: True), True/False): ')

        if enabled:
            enabled = enabled.strip()
            if enabled.lower() in ['true', 'false']:
                return enabled.lower() == 'true'
            elif enabled.lower() not in ['true', 'false']:
                print('Enabled status must be either true or false.')
                print('If you do not want to set enabled status, leave the field blank.')
                continue
        return True
