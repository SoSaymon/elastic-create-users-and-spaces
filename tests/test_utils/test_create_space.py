import pytest
import sys

sys.path.append("..")

from src.utils.create_space import prepare_payload, create_space


@pytest.mark.space
class TestCreateSpace:
    @pytest.mark.parametrize(
        "space_id, space_name, description, initials, color, disabled_features, image_url, expected",
        [
            (
                "test_space_id",
                "test_space_name",
                "test_description",
                "TI",
                "#FFFFFF",
                None,
                None,
                {
                    "id": "test_space_id",
                    "name": "test_space_name",
                    "description": "test_description",
                    "initials": "TI",
                    "color": "#FFFFFF",
                },
            ),
        ],
    )
    def test_prepare_payload(
        self,
        space_id: str,
        space_name: str,
        description: str,
        initials: str,
        color: str,
        disabled_features: list,
        image_url: str,
        expected: dict,
    ) -> None:
        """
        Test prepare_payload function.
        :param space_id:  Space ID.
        :param space_name:  Space name.
        :param description:  Space description.
        :param initials:  Space initials.
        :param color:  Space color.
        :param disabled_features:  Space disabled features.
        :param image_url:  Space image URL.
        :param expected:  Expected payload.
        :return:  None.
        """
        assert (
            prepare_payload(
                space_id,
                space_name,
                description,
                initials,
                color,
                disabled_features,
                image_url
            )
            == expected
        )

    @pytest.mark.parametrize(
        "payload, expected",
        [
            (
                {
                    "id": "test_space_id",
                    "name": "test_space_name",
                    "description": "test_description",
                    "initials": "TI",
                    "color": "#FFFFFF",
                },
                None,
            ),
        ],
    )
    def test_create_space(
        self,
        payload: dict,
        expected: None,
    ) -> None:
        """
        Test create_space function.
        :param payload:  Payload.
        :param expected:  Expected payload.
        :return:  None.
        """
        assert create_space(payload) == expected