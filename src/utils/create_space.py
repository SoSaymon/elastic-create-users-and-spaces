from typing import Dict

import requests

from .load_env import get_all_env


def prepare_payload(
        space_id: str,
        space_name: str,
        description: str | None = None,
        initials: str | None = None,
        color: str | None = None,
        disabled_features: list | None = None,
        image_url: str | None = None,
) -> Dict[str, str]:
    """
    Prepare payload for space creation.

    :param space_id:  Space ID.
    :param space_name:  Space name.
    :param description:  Space description.
    :param initials:  Space initials.
    :param color:  Space color.
    :param disabled_features:  Space disabled features.
    :param image_url:  Space image URL.
    :return:  Payload.
    """
    payload = {
        "id": space_id,
        "name": space_name,
    }

    if description:
        payload['description'] = description
    if initials:
        payload['initials'] = initials
    if color:
        payload['color'] = color
    if disabled_features:
        payload['disabledFeatures'] = disabled_features
    if image_url:
        payload['imageUrl'] = image_url

    return payload


def create_space(payload: Dict[str, str]) -> None:
    """
    Create space via Kibana API.

    :param payload: Payload.
    :return: None.
    """
    elastic_url, kibana_url, username, password = get_all_env()
    headers = {
        'Content-Type': 'application/json',
        'kbn-xsrf': 'true',
    }

    try:
        response = requests.post(
            f'{kibana_url}api/spaces/space',
            auth=(username, password),
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            print(f'Space {payload.get("name")} created successfully.')
        else:
            raise requests.RequestException(response.text)
    except requests.RequestException as err:
        print(f'Error creating space {payload.get("name")}.')
        print(err)
