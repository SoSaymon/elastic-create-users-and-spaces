import pytest
import sys

sys.path.append("..")

from src.utils.create_users import User


@pytest.fixture
def user() -> User:
    """
    Fixture for User class
    :return:  User object
    """
    return User(
        username="test_user",
        roles=["test_role"],
        password="test_password",
        password_hash=None,
        full_name="test_full_name",
        email="test_email@test.com",
        metadata={"test_key": "test_value"},
        enabled=True,
    )


@pytest.fixture()
def user_disabled() -> User:
    """
    Fixture for User class (disabled)
    :return:  User object
    """
    return User(
        username="test_user_disabled",
        roles=["test_role"],
        password="test_password",
        password_hash=None,
        full_name="test_full_name_disabled",
        email="test_email@test.com",
        metadata={"test_key": "test_value"},
        enabled=False,
    )


@pytest.mark.es_user
class TestUser:
    def test_user(self, user: User) -> None:
        assert user._username == "test_user"
        assert user._roles == ["test_role"]
        assert user._password == "test_password"
        assert user._password_hash is None
        assert user._full_name == "test_full_name"
        assert user._email == "test_email@test.com"
        assert user._metadata == {"test_key": "test_value"}
        assert user._enabled is True

    def test_user_str(self, user: User) -> None:
        """
        Test __str__ method
        :param user:  User object
        :return:  None
        """
        assert str(
            user) == "User(username=test_user, roles=['test_role'], password=test_password, password_hash=None, full_name=test_full_name, email=test_email@test.com, metadata={'test_key': 'test_value'}, enabled=True)"

    def test_user_prepare_payload(self, user: User) -> None:
        """
        Test prepare_payload method
        :param user:  User object
        :return:  None
        """
        assert user.prepare_payload() == {
            "password": "test_password",
            "roles": ["test_role"],
            "full_name": "test_full_name",
            "email": "test_email@test.com",
            "metadata": {"test_key": "test_value"},
        }

    def test_create_user(self, user: User) -> None:
        """
        Test create method
        :param user:  User object
        :return:  None
        """
        assert user.create() is None

    def test_user_disabled(self, user_disabled: User) -> None:
        """
        Test User class (disabled)
        :param user_disabled:  User object
        :return:  None
        """
        assert user_disabled._username == "test_user_disabled"
        assert user_disabled._roles == ["test_role"]
        assert user_disabled._password == "test_password"
        assert user_disabled._password_hash is None
        assert user_disabled._full_name == "test_full_name_disabled"
        assert user_disabled._email == "test_email@test.com"
        assert user_disabled._metadata == {"test_key": "test_value"}
        assert user_disabled._enabled is False

    def test_user_disabled_str(self, user_disabled: User) -> None:
        """
        Test __str__ method (disabled user)
        :param user_disabled:  User object
        :return:  None
        """
        assert str(
            user_disabled) == "User(username=test_user_disabled, roles=['test_role'], password=test_password, password_hash=None, full_name=test_full_name_disabled, email=test_email@test.com, metadata={'test_key': 'test_value'}, enabled=False)"

    def test_user_disabled_prepare_payload(self, user_disabled: User) -> None:
        """
        Test prepare_payload method (disabled user)
        :param user_disabled:  User object
        :return:  None
        """
        assert user_disabled.prepare_payload() == {
            "password": "test_password",
            "roles": ["test_role"],
            "full_name": "test_full_name_disabled",
            "email": "test_email@test.com",
            "metadata": {"test_key": "test_value"},
            "enabled": False
        }

    def test_create_user_disabled(self, user_disabled: User) -> None:
        """
        Test create method (disabled user)
        :param user_disabled:  User object
        :return:  None
        """
        assert user_disabled.create() is None
