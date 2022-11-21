from typing import List

import pytest
from pytest_mock import MockerFixture

from achievement_1001_jackalopes import sprintf_dna


def test_sprintf_dna(mocker: MockerFixture) -> None:
    mocker.patch("achievement_1001_jackalopes.GENES", ["Pet", "Clown", "Fewlock"])

    result = sprintf_dna([0, 1, 2, 2, 0, 1])

    assert result == "Pet Clown Fewlock Fewlock Pet Clown"
