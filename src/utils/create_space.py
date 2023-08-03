import requests

from src.utils.load_env import get_all_env


def prepare_payload(
        space_id: str,
        space_name: str,
        description: str = None,
        initials: str = None,
        color: str = None,
        disabled_features: list = None,
        image_url: str = None,
) -> dict:
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


def create_space(payload: dict) -> None:
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
