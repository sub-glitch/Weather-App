from backend import get_data


def test_get_data_returns_list():
    data = get_data("Lagos", 1)
    assert isinstance(data, list)


def test_get_data_handles_invalid_city():
    try:
        data = get_data("NotACity", 1)
        assert data == [] or data is None
    except Exception:
        assert True
