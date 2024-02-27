import os
from io import StringIO
from dotenv import load_dotenv


def test_insert_new_environment_values():

    environment_key: str = 'TEST'
    environment_value: str = 'FOO'

    config = StringIO(
        f"{environment_key}={environment_value}"
    )

    load_dotenv(stream=config)

    assert os.getenv(environment_key)
    assert os.getenv(environment_key) == environment_value


def test_return_environment_value(env_value='MEMBERS'):
    load_dotenv()

    assert os.getenv(env_value) == 'https://www.googleapis.com/auth/admin.directory.group.member'  # noqa: E501
