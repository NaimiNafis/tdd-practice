from caesar_cipher import caesar_cipher


def test_shifts_lowercase():
    assert caesar_cipher("abc", 1) == "bcd"


def test_wraps_around_lowercase():
    assert caesar_cipher("xyz", 3) == "abc"


def test_preserves_case():
    assert caesar_cipher("Hello", 13) == "Uryyb"


def test_non_alpha_unchanged():
    assert caesar_cipher("Hello, World!", 5) == "Mjqqt, Btwqi!"


def test_zero_shift():
    assert caesar_cipher("abc", 0) == "abc"


def test_shifts_uppercase():
    assert caesar_cipher("ABC", 1) == "BCD"


def test_wraps_around_uppercase():
    assert caesar_cipher("XYZ", 3) == "ABC"


def test_empty_string():
    assert caesar_cipher("", 5) == ""
