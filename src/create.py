import argparse

from utils.get_mode_options import get_mode_options
from utils.create_space import create_space, prepare_payload
from utils.create_users import User


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='create.py',
        usage='%(prog)s [options]',
        description='Create a Kibana Spaces and Elasticsearch Users.',
        epilog='Enjoy the program! :)',
    )

    parser.add_argument(
        'mode',
        type=str,
        choices=['space', 'user'],
        help='The mode to run the script in. Required.',
    )

    args = parser.parse_args()
    mode = args.mode

    if mode == 'space':
        space_id, space_name, description, initials, color, disabled_features, image_url = get_mode_options("space")
        payload = prepare_payload(
            space_id=space_id,
            space_name=space_name,
            description=description,
            initials=initials,
            color=color,
            disabled_features=disabled_features,
            image_url=image_url,
        )
        create_space(payload)
    elif mode == 'user':
        username, roles, password, password_hash, full_name, email, metadata, enabled = get_mode_options("user")
        user = User(
            username=username,
            roles=roles,
            password=password,
            password_hash=password_hash,
            full_name=full_name,
            email=email,
            metadata=metadata,
            enabled=enabled,
        )
        user.create()
    else:
        raise ValueError(f"Invalid mode: {mode}, must be one of 'space' or 'user'")


if __name__ == '__main__':
    main()