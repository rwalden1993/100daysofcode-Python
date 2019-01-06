from unittest.mock import patch
import pytest
from datetime import date

from schedule import schedule, add_event

@patch("builtins.input", side_effect=['1993-01-28', 'birthday', 'birthday', '1993-01-28'])
def test_add_event(inp):
    add_event()
    assert schedule['birthday'] ==  date.fromisoformat('1993-01-28')

    with pytest.raises(ValueError):
        add_event()