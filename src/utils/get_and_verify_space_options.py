import re
from typing import List, Tuple, Optional, Callable

from .space_options_utils.verifiers import verify, verify_space_id, verify_initials_len, \
    verify_if_color_starts_with_hash, verify_if_color_has_seven_characters, verify_color_regex_pattern, \
    verify_if_string_starts_with_comma, verify_if_space_exists_near_comma, verify_if_string_ends_with_comma, \
    verify_disabled_features_regex_pattern, verify_if_image_url_is_base64_encoded, \
    verify_if_image_url_has_image_type, verify_if_image_url_starts_with_data_image

from .space_options_utils.utils import get_image_url_image_type, get_input

SPACE_ID = str
SPACE_NAME = str
DESCRIPTION = Optional[str]
INITIALS = Optional[str]
COLOR = Optional[str]
DISABLED_FEATURES = Optional[List[str]]
IMAGE_URL = Optional[str]

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


def get_and_verify_space_id(get_space_id_fn: Callable[[str], str] = get_input) -> SPACE_ID:
    """
    Get and verify the space ID

    :return:  String space ID
    """
    while True:
        space_id = get_space_id_fn('Enter the space ID (Required): ')
        space_id = space_id.strip().lower()

        if verify_space_id(space_id):
            return space_id
        print('Space ID is required.')


def get_and_verify_space_name(get_space_name_fn: Callable[[str], str] = get_input) -> SPACE_NAME:
    """
    Get and verify the space name

    :return:  String space name
    """
    while True:
        space_name = get_space_name_fn('Enter the space name (Required): ')
        space_name = space_name.strip()

        if verify(space_name):
            return space_name
        print('Space name is required.')


def get_and_verify_description(get_space_description: Callable[[str], str] = get_input) -> DESCRIPTION:
    """
    Get and verify the description

    :return:  String description or None
    """
    description = get_space_description('Enter the space description (Optional): ')
    description = description.strip()

    if verify(description):
        return description
    return None


def get_and_verify_initials(get_space_initials_fn: Callable[[str], str] = get_input) -> INITIALS:
    """
    Get and verify the initials

    :return:  String initials or None
    """
    while True:
        initials = get_space_initials_fn('Enter the space initials (Optional, max length 2): ')
        initials = initials.strip()

        if verify(initials):

            if verify_initials_len(initials):
                return initials.upper()
            else:
                print('Initials must be between 1 and 2 characters. Example: CJ or C')
                print('If you do not want to set initials, leave the field blank.')
                continue
        return None


def get_and_verify_color(get_space_color_fn: Callable[[str], str] = get_input) -> COLOR:
    """
    Get and verify the color

    :return:  String hex color or None
    """
    while True:
        color = get_space_color_fn('Enter the space color (Optional, hex format): ')
        color = color.strip()

        if verify(color):

            if not verify_if_color_starts_with_hash(color):
                color = f'#{color}'

            if not verify_if_color_has_seven_characters(color):
                color = color[0] + color[1] + color[1] + color[2] + color[2] + color[3] + color[3]

            if verify_color_regex_pattern(color):
                return color
            else:
                print('Color must be in hex format. Example: #000000')
                print('If you do not want to set a color, leave the field blank.')
                continue
        return None


def get_and_verify_disabled_features(
        get_space_disabled_features_fn: Callable[[str], str] = get_input) -> DISABLED_FEATURES:
    """
    Get and verify the disabled features

    :return:  List of disabled features or None
    """
    while True:
        disabled_features = get_space_disabled_features_fn(
            'Enter the space disabled features (Optional, comma separated): ')
        disabled_features = disabled_features.strip()

        if verify(disabled_features):

            if verify_if_space_exists_near_comma(disabled_features):
                disabled_features = disabled_features.replace(', ', ',')
                disabled_features = disabled_features.replace(' ,', ',')

            if verify_if_string_starts_with_comma(disabled_features):
                disabled_features = disabled_features[1:]

            if verify_if_string_ends_with_comma(disabled_features):
                disabled_features = disabled_features[:-1]

            if verify_disabled_features_regex_pattern(disabled_features):
                return disabled_features.split(',')
            else:
                print('Disabled features must be comma separated. Example: feature1,feature2')
                print('If you do not want to set disabled features, leave the field blank.')
                continue
        return None


def get_and_verify_image_url(get_space_image_url_fn: Callable[[str], str] = get_input) -> IMAGE_URL:
    """
    Get and verify the image URL

    :return:  String image URL or None
    """
    valid_image_types: List[str] = ["png", "jpeg", "gif", "webp"]

    while True:
        image_url = get_space_image_url_fn('Enter the space image URL (Optional): ')
        image_url = image_url.strip()

        if verify(image_url):

            if not verify_if_image_url_starts_with_data_image(image_url):
                print("Image URL must start with 'data:image'")
                print('If you do not want to set an image URL, leave the field blank.')
                continue

            if not verify_if_image_url_has_image_type(image_url):
                print("Image URL must have a image type")
                print('If you do not want to set an image URL, leave the field blank.')
                continue

            if get_image_url_image_type(image_url) not in valid_image_types:
                print("Image URL must have a valid image type (png, jpeg, gif, webp)")
                print('If you do not want to set an image URL, leave the field blank.')
                continue

            if not verify_if_image_url_is_base64_encoded(image_url):
                print("Image URL must be base64 encoded")
                print('If you do not want to set an image URL, leave the field blank.')
                continue
            return image_url
        return None
