import pytest

from gnew_coreutils import true


def test_true() -> None:
    with pytest.raises(SystemExit) as err_info:
        true()

    assert err_info.value.code == 0, "error code wasn't success"
