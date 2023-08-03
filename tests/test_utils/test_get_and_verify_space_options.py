import pytest
import sys

from pytest_mock import MockFixture

sys.path.append("..")

from src.utils.get_and_verify_space_options import get_and_verify_space_id, \
    get_and_verify_space_name, get_and_verify_description, get_and_verify_initials, get_and_verify_color, \
    get_and_verify_disabled_features, get_and_verify_image_url


@pytest.mark.space_options
class TestSpaceOptions:
    @pytest.mark.parametrize(
        "space_id, expected",
        [
            ('test', 'test'),
            ('test ', 'test'),
            (' test', 'test'),
            (' test ', 'test'),
            ('test-test', 'test-test'),
            ('test_test', 'test_test'),
            ('test-test_test', 'test-test_test'),
            ('test_test-test', 'test_test-test'),
            ('test_123', 'test_123'),
            ('test-123', 'test-123'),
            ('test_123-test', 'test_123-test'),
            ('test-test_123', 'test-test_123'),
        ],
    )
    def test_get_and_verify_space_id(self, mocker: MockFixture, space_id: str, expected: str):
        mocker.patch("builtins.input", return_value=space_id)
        assert get_and_verify_space_id() == expected

    # TODO: Fix this test
    # @pytest.mark.parametrize(
    #     "space_id",
    #     [
    #         '',
    #         ' ',
    #         '  ',
    #         'invalid space id',
    #         '!@#$%^&*()',
    #         'test.test',
    #     ]
    # )
    # def test_get_and_verify_space_id_invalid(self, mocker: MockFixture, space_id: str):
    #     mocker.patch("builtins.input", return_value=space_id)
    #     assert get_and_verify_space_id() is None

    @pytest.mark.parametrize(
        "space_name, expected",
        [
            ('test', 'test'),
            ('test ', 'test'),
            (' test', 'test'),
            (' test ', 'test'),
            ('test-test', 'test-test'),
            ('test_test', 'test_test'),
            ('test-test_test', 'test-test_test'),
            ('test_test-test', 'test_test-test'),
            ('test_123', 'test_123'),
            ('test-123', 'test-123'),
            ('test_123-test', 'test_123-test'),
            ('test-test_123', 'test-test_123'),
        ],
    )
    def test_get_and_verify_space_name(self, mocker: MockFixture, space_name: str, expected: str):
        mocker.patch("builtins.input", return_value=space_name)
        assert get_and_verify_space_name() == expected

    @pytest.mark.parametrize(
        "description, expected",
        [
            ('test', 'test'),
            ('test ', 'test'),
            (' test', 'test'),
            (' test ', 'test'),
            ('test-test', 'test-test'),
            ('test_test', 'test_test'),
            ('test-test_test', 'test-test_test'),
            ('test_test-test', 'test_test-test'),
            ('test_123', 'test_123'),
            ('test-123', 'test-123'),
            ('test_123-test', 'test_123-test'),
            ('test-test_123', 'test-test_123'),
        ],
    )
    def test_get_and_verify_description(self, mocker: MockFixture, description: str, expected: str):
        mocker.patch("builtins.input", return_value=description)
        assert get_and_verify_description() == expected

    @pytest.mark.parametrize(
        "initials, expected",
        [
            ('T', 'T'),
            ('T ', 'T'),
            (' T', 'T'),
            (' T ', 'T'),
            ('TT', 'TT'),
            ('TT ', 'TT'),
            (' TT', 'TT'),
            (' TT ', 'TT'),
            ('t', 'T'),
            ('t ', 'T'),
            (' t', 'T'),
            (' t ', 'T'),
            ('tt', 'TT'),
            ('tt ', 'TT'),
            (' tt', 'TT'),
            (' tt ', 'TT'),
            ('tT', 'TT'),
            ('tT ', 'TT'),
            (' tT', 'TT'),
            (' tT ', 'TT'),
            ('Tt', 'TT'),
            ('Tt ', 'TT'),
            (' Tt', 'TT'),
            (' Tt ', 'TT'),
        ],
    )
    def test_get_and_verify_initials(self, mocker: MockFixture, initials: str, expected: str):
        mocker.patch("builtins.input", return_value=initials)
        assert get_and_verify_initials() == expected

    @pytest.mark.parametrize(
        "color, expected",
        [
            ('#000000', '#000000'),
            ('#000000 ', '#000000'),
            (' #000000', '#000000'),
            (' #000000 ', '#000000'),
            ('#000', '#000'),
            ('#000 ', '#000'),
            (' #000', '#000'),
            (' #000 ', '#000'),
            ('000', '#000'),
            ('000 ', '#000'),
            (' 000', '#000'),
            (' 000 ', '#000'),
            ('000000', '#000000'),
            ('000000 ', '#000000'),
            (' 000000', '#000000'),
            (' 000000 ', '#000000'),
            ],
    )
    def test_get_and_verify_color(self, mocker: MockFixture, color: str, expected: str):
        mocker.patch("builtins.input", return_value=color)
        assert get_and_verify_color() == expected

    @pytest.mark.parametrize(
        "disabled_features, expected",
        [
            ('test', ['test']),
            ('test ', ['test']),
            (' test', ['test']),
            (' test ', ['test']),
            ('test,test', ['test', 'test']),
            ('test,test ', ['test', 'test']),
            (' test,test', ['test', 'test']),
            (' test,test ', ['test', 'test']),
            ('test, test', ['test', 'test']),
            ('test, test ', ['test', 'test']),
            (' test, test', ['test', 'test']),
            (' test, test ', ['test', 'test']),
            (',test', ['test']),
            (' ,test', ['test']),
            (', test', ['test']),
            (' , test', ['test']),
            (',test,', ['test']),
            (' ,test,', ['test']),
            (', test,', ['test']),
            (' , test,', ['test']),
            (',test, ', ['test']),
            (' ,test, ', ['test']),
            (', test, ', ['test']),
            (' , test, ', ['test']),
            (',test ,', ['test']),
            (' ,test ,', ['test']),
            (', test ,', ['test']),
            (' , test ,', ['test']),
            (',test , ', ['test']),
            (' ,test , ', ['test']),
        ],
    )
    def test_get_and_verify_disabled_features(self, mocker: MockFixture, disabled_features: str, expected: str):
        mocker.patch("builtins.input", return_value=disabled_features)
        assert get_and_verify_disabled_features() == expected

