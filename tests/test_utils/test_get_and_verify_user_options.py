import pytest
import sys

from pytest_mock import MockFixture

sys.path.append("..")

from src.utils.get_and_verify_user_options import get_and_verify_username, get_and_verify_roles, get_and_verify_password, get_and_verify_password_hash, get_and_verify_full_name, get_and_verify_email, get_and_verify_metadata, get_and_verify_enabled


@pytest.mark.user_options
class TestUserOptions:
    @pytest.mark.parametrize(
        "username, expected",
        [
            ("test", "test"),
            ("test ", "test"),
            (" test", "test"),
            (" test ", "test"),
            ("test1", "test1"),
            ("test1 ", "test1"),
            (" test1", "test1"),
            (" test1 ", "test1"),
            ("test_1", "test_1"),
        ]
    )
    def test_get_and_verify_username(self, mocker: MockFixture, username: str, expected: str) -> None:
        mocker.patch("builtins.input", return_value=username)
        assert get_and_verify_username() == expected

    @pytest.mark.parametrize(
        "roles, expected",
        [
            ("test", ["test"]),
            ("test ", ["test"]),
            (" test", ["test"]),
            (" test ", ["test"]),
            ("test1,test2", ["test1", "test2"]),
            ("test1,test2 ", ["test1", "test2"]),
            (" test1,test2", ["test1", "test2"]),
            (" test1,test2 ", ["test1", "test2"]),
            ("test_1,test_2", ["test_1", "test_2"]),
        ]
    )
    def test_get_and_verify_roles(self, mocker: MockFixture, roles: str, expected: list) -> None:
        mocker.patch("builtins.input", return_value=roles)
        assert get_and_verify_roles() == expected

    @pytest.mark.parametrize(
        "password, expected",
        [
            ("test123", "test123"),
            ("test123 ", "test123"),
            (" test123", "test123"),
            (" test123 ", "test123"),
            ("test1234", "test1234"),
        ]
    )
    def test_get_and_verify_password(self, mocker: MockFixture, password: str, expected: str) -> None:
        mocker.patch("builtins.input", return_value=password)
        assert get_and_verify_password() == expected

    @pytest.mark.parametrize(
        "password_hash, expected",
        [
            ("test123", "test123"),
            ("test123 ", "test123"),
            (" test123", "test123"),
            (" test123 ", "test123"),
            ("test1234", "test1234"),
        ]
    )
    def test_get_and_verify_password_hash(self, mocker: MockFixture, password_hash: str, expected: str) -> None:
        mocker.patch("builtins.input", return_value=password_hash)
        assert get_and_verify_password_hash() == expected


    @pytest.mark.parametrize(
        "full_name, expected",
        [
            ("John Doe", "John Doe"),
            ("John Doe ", "John Doe"),
            (" John Doe", "John Doe"),
            (" John Doe ", "John Doe"),
        ],
    )
    def test_get_and_verify_full_name(self, mocker: MockFixture, full_name: str, expected: str) -> None:
        mocker.patch("builtins.input", return_value=full_name)
        assert get_and_verify_full_name() == expected

    @pytest.mark.parametrize(
        "email, expected",
        [
            ("john.doe@test.com", "john.doe@test.com"),
            ("john.doe@test.com ", "john.doe@test.com"),
            (" john.doe@test.com", "john.doe@test.com"),
            (" john.doe@test.com ", "john.doe@test.com"),
        ],
    )
    def test_get_and_verify_email(self, mocker: MockFixture, email: str, expected: str) -> None:
        mocker.patch("builtins.input", return_value=email)
        assert get_and_verify_email() == expected


    @pytest.mark.parametrize(
        "metadata, expected",
        [
            ("test:value", {"test": "value"}),
            ("test:value ", {"test": "value"}),
            (" test:value", {"test": "value"}),
            (" test:value ", {"test": "value"}),
            ("test1:value1,test2:value2", {"test1": "value1", "test2": "value2"}),
            ("test1:value1,test2:value2 ", {"test1": "value1", "test2": "value2"}),
            (" test1:value1,test2:value2", {"test1": "value1", "test2": "value2"}),
            (" test1:value1,test2:value2 ", {"test1": "value1", "test2": "value2"}),
            ("test_1:value_1, test_2:value_2", {"test_1": "value_1", "test_2": "value_2"}),
            ("test_1:value_1 ,test_2:value_2", {"test_1": "value_1", "test_2": "value_2"}),
            ("test_1:value_1 , test_2:value_2", {"test_1": "value_1", "test_2": "value_2"}),
        ],
    )
    def test_get_and_verify_metadata(self, mocker: MockFixture, metadata: str, expected: dict) -> None:
        mocker.patch("builtins.input", return_value=metadata)
        assert get_and_verify_metadata() == expected

    @pytest.mark.parametrize(
        "enabled, expected",
        [
            ("true", True),
            ("true ", True),
            (" true", True),
            (" true ", True),
            ("false", False),
            ("false ", False),
            (" false", False),
            (" false ", False),
            ("True", True),
            ("False", False),
        ],
    )
    def test_get_and_verify_enabled(self, mocker: MockFixture, enabled: str, expected: bool) -> None:
        mocker.patch("builtins.input", return_value=enabled)
        assert get_and_verify_enabled() == expected
