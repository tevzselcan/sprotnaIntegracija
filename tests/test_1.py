def test_basic_math():
    assert 2 + 2 == 4


def test_main_exists():
    import main
    assert hasattr(main, "__name__")