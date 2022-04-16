from unittest.mock import MagicMock

import pytest
from pytest_mock.plugin import MockerFixture

from {{cookiecutter.project_slug}}.main import greet


@pytest.fixture()
def mocked_greet(mocker: MockerFixture) -> MagicMock:
    mocked = mocker.patch("typer.echo")
    greet(name="Huba")
    return mocked


def test_greet_positive(mocked_greet: MagicMock) -> None:
    mocked_greet.assert_called_with("Welcome Huba!")


def test_greet_negative(mocked_greet: MagicMock) -> None:
    with pytest.raises(AssertionError):
        mocked_greet.assert_called_with("Welcome Ruba!")
