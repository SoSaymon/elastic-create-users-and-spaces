from typing import Any, Dict, List

import requests

from src.utils.load_env import get_all_env


class User:
    def __init__(
            self,
            username: str,
            roles: List[str],
            password: str = None,
            password_hash: str = None,
            full_name: str = None,
            email: str = None,
            metadata: dict = None,
            enabled: bool = True,
    ) -> None:
        """
        Create an Elasticsearch user.

        :param username:  The username of the user to create. Required.
        :param roles:  The roles of the user to create. Required.
        :param password:  The password of the user to create. Required if password_hash is not specified.
        :param password_hash:  The password hash of the user to create. Required if password is not specified.
        :param full_name:  The full name of the user to create. Optional.
        :param email:  The email of the user to create. Optional.
        :param metadata:  The metadata of the user to create. Optional.
        :param enabled:  Whether the user is enabled. Optional. Defaults to True.
        :return:  None
        :raises ValueError: If both password and password_hash are specified.
            If no roles are specified.
        """
        self._username = username
        self._roles = roles
        self._password = password
        self._password_hash = password_hash
        self._full_name = full_name
        self._email = email
        self._metadata = metadata
        self._enabled = enabled

        self.validate_password()
        self.validate_roles()

    def __str__(self):
        return f"User(username={self._username}, roles={self._roles}, password={self._password}, password_hash={self._password_hash}, full_name={self._full_name}, email={self._email}, metadata={self._metadata}, enabled={self._enabled})"

    def prepare_payload(self) -> Dict[str, Any]:
        """
        Prepare the request body for the Elasticsearch API user creation request.

        :return: The request body.
        """
        request_body = {}

        if self._password:
            request_body['password'] = self._password
        if self._password_hash:
            request_body['password_hash'] = self._password_hash
        if self._roles:
            request_body['roles'] = self._roles
        if self._full_name:
            request_body['full_name'] = self._full_name
        if self._email:
            request_body['email'] = self._email
        if self._metadata:
            request_body['metadata'] = self._metadata
        if not self._enabled:
            request_body['enabled'] = self._enabled

        return request_body

    def create(self) -> None:
        """
        Create the user in Elasticsearch.

        :return: None
        :raises requests.exceptions.HTTPError: If the request fails.
        """
        elastic_url, kibana_url, username, password = get_all_env()
        url = f"{elastic_url}_security/user/{self._username}"
        request_body = self.prepare_payload()

        response = requests.post(
            url,
            auth=(username, password),
            headers={'Content-Type': 'application/json'},
            json=request_body
        )
        if response.status_code == 200:
            print(f"User {self._username} created successfully.")
        else:
            raise requests.exceptions.HTTPError(f"User {self._username} creation failed. Response: {response.text}")

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        self._username = value

    @property
    def roles(self) -> List[str]:
        return self._roles

    @roles.setter
    def roles(self, value: List[str]) -> None:
        self._roles = value
        self.validate_roles()

    def validate_roles(self) -> None:
        """
        Validate that the roles are not empty.

        :return: None
        :raises ValueError: If no roles are specified.
        """
        if len(self._roles) == 0:
            raise ValueError('Must specify at least one role.')

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        self._password = value
        self.validate_password()

    def validate_password(self) -> None:
        """
        Validate that the password and password_hash are not both specified.

        :return: None
        :raises ValueError: If both password and password_hash are specified.
        """
        if self._password_hash is not None and self._password is not None:
            raise ValueError('Cannot specify both password and password_hash.')

    @property
    def password_hash(self) -> str:
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value: str) -> None:
        self._password_hash = value
        self.validate_password()

    @property
    def full_name(self) -> str:
        return self._full_name

    @full_name.setter
    def full_name(self, value: str) -> None:
        self._full_name = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    @property
    def metadata(self) -> dict:
        return self._metadata

    @metadata.setter
    def metadata(self, value: dict) -> None:
        self._metadata = value

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value
