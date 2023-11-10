import sys
from typing import List, Tuple, Dict, Any, Union

sys.path.append('..')

from .get_and_verify_space_options import get_and_verify_space_options
from .get_and_verify_user_options import get_and_verify_user_options

SPACE_ID = str
SPACE_NAME = str
DESCRIPTION = str | None
INITIALS = str | None
COLOR = str | None
DISABLED_FEATURES = List[str] | None
IMAGE_URL = str | None

SpaceData = Tuple[SPACE_ID, SPACE_NAME, DESCRIPTION, INITIALS, COLOR, DISABLED_FEATURES, IMAGE_URL]

USERNAME = str
ROLES = List[str]
PASSWORD = str | None
PASSWORD_HASH = str | None
FULL_NAME = str | None
EMAIL = str | None
METADATA = Dict[str, Any] | None
ENABLED = bool

UserData = Tuple[USERNAME, ROLES, PASSWORD, PASSWORD_HASH, FULL_NAME, EMAIL, METADATA, ENABLED]


def get_mode_options(mode: str) -> Union[SpaceData, UserData]:
    """
    Get user options for space or user mode.

    :param mode:  The mode to run the script in. Required.
    :return:  A tuple of user options.
    """
    if mode == 'space':
        return get_and_verify_space_options()
    elif mode == 'user':
        return get_and_verify_user_options()

    raise ValueError('Mode must be space or user.')
