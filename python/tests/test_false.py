import pytest

from gnew_coreutils import false


def test_false() -> None:
    with pytest.raises(SystemExit) as err_info:
        false()

    assert err_info.value.code != 0, "error code wasn't a failure"
