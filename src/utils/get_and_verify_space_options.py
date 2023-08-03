import re
from typing import List, Tuple

SPACE_ID = str
SPACE_NAME = str
DESCRIPTION = str | None
INITIALS = str | None
COLOR = str | None
DISABLED_FEATURES = List[str] | None
IMAGE_URL = str | None

SpaceData = Tuple[SPACE_ID, SPACE_NAME, DESCRIPTION, INITIALS, COLOR, DISABLED_FEATURES, IMAGE_URL]


def get_and_verify_space_options() -> SpaceData:
    """
    Get space options.
    :return:  A tuple of space options.
    """
    space_id = get_and_verify_space_id()
    space_name = get_and_verify_space_name()
    description = get_and_verify_description()
    initials = get_and_verify_initials()
    color = get_and_verify_color()
    disabled_features = get_and_verify_disabled_features()
    image_url = get_and_verify_image_url()

    return space_id, space_name, description, initials, color, disabled_features, image_url


def get_and_verify_space_id() -> SPACE_ID:
    """
    Get and verify the space ID
    :return:  String space ID
    """
    while True:
        space_id = input('Enter the space ID (Required): ')

        if space_id:
            space_id = space_id.strip().lower()

            pattern = r'^[a-z0-9_-]+$'
            if re.match(pattern, space_id):
                return space_id
        print('Space ID is required.')


def get_and_verify_space_name() -> SPACE_NAME:
    """
    Get and verify the space name
    :return:  String space name
    """
    while True:
        space_name = input('Enter the space name (Required): ')

        if space_name:
            space_name = space_name.strip()
            return space_name
        print('Space name is required.')


def get_and_verify_description() -> DESCRIPTION:
    """
    Get and verify the description
    :return:  String description or None
    """
    description = input('Enter the space description (Optional): ')

    if description:
        description = description.strip()
        return description
    return None


def get_and_verify_initials() -> INITIALS:
    """
    Get and verify the initials
    :return:  String initials or None
    """
    while True:
        initials = input('Enter the space initials (Optional, max length 2): ')

        if initials:
            initials = initials.strip()

            if 1 <= len(initials) <= 2 and initials.isalpha():
                return initials.upper()
            elif not 1 <= len(initials) <= 2:
                print('Initials must be between 1 and 2 characters. Example: CJ or C')
                print('If you do not want to set initials, leave the field blank.')
                continue
        return None


def get_and_verify_color() -> COLOR:
    """
    Get and verify the color
    :return:  String hex color or None
    """
    while True:
        color = input('Enter the space color in hex format (Optional): ')

        if color:
            color = color.strip()

            if not color.startswith('#'):
                color = f'#{color}'

            if not len(color) == 7:
                color = color[0] + color[1] + color[1] + color[2] + color[2] + color[3] + color[3]


            pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
            if re.match(pattern, color):
                return color
            elif not re.match(pattern, color) and color != '':
                print('Color must be in hex format. Example: #000000')
                print('If you do not want to set a color, leave the field blank.')
                continue
        return None


def get_and_verify_disabled_features() -> DISABLED_FEATURES:
    """
    Get and verify the disabled features
    :return:  List of disabled features or None
    """
    while True:
        disabled_features = input('Enter the space disabled features (Optional, comma separated): ')

        if disabled_features:
            disabled_features = disabled_features.strip()

            if re.search(r',\s', disabled_features):
                disabled_features = disabled_features.replace(', ', ',')

            if re.search(r'\s,', disabled_features):
                disabled_features = disabled_features.replace(' ,', ',')

            if disabled_features.startswith(','):
                disabled_features = disabled_features[1:]

            if disabled_features.endswith(','):
                disabled_features = disabled_features[:-1]

            pattern = r'^[a-zA-Z0-9_-]+(,[a-zA-Z0-9_-]+)*$'
            if re.match(pattern, disabled_features):
                return disabled_features.split(',')
            elif not re.match(pattern, disabled_features) and disabled_features != '':
                print('Disabled features must be comma separated. Example: feature1,feature2')
                print('If you do not want to set disabled features, leave the field blank.')
                continue
        return None


def get_and_verify_image_url() -> IMAGE_URL:
    """
    Get and verify the image URL
    :return:  String image URL or None
    """
    while True:
        image_url = input('Enter the space image URL (Optional): ')

        if image_url:
            image_url = image_url.strip()

            if not image_url.startswith("data:image/"):
                print("Image URL must start with 'data:image'")
                print('If you do not want to set an image URL, leave the field blank.')
                continue

            image_type_match = re.match(r"data:image/(\w+);", image_url)
            if not image_type_match:
                print("Image URL must have a valid image type")
                print('If you do not want to set an image URL, leave the field blank.')
                continue

            image_type = image_type_match.group(1)
            if image_type not in ["png", "jpeg", "gif", "webp"]:
                print("Image URL must have a valid image type")
                print('If you do not want to set an image URL, leave the field blank.')
                continue

            if not re.search(r"base64,", image_url):
                print("Image URL must be base64 encoded")
                print('If you do not want to set an image URL, leave the field blank.')
                continue
            return image_url
        return None
