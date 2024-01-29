import os

import pytest

from ....bioterm.common.core.config import getenv_boolean


@pytest.mark.parametrize(
    "env_value,expected_result",
    [
        ("TRUE", True),
        ("tRuE", True),
        ("1", True),
        ("FALSE", False),
        ("other_value", False),
        (None, True),  # Test with an environment variable not set, using default value
    ],
)
def test_getenv_boolean(env_value, expected_result):
    if env_value is not None:
        os.environ["TEST_VAR"] = env_value
    else:
        os.environ.pop("TEST_VAR", None)  # Ensure it's removed if set

    assert getenv_boolean("TEST_VAR") == expected_result
