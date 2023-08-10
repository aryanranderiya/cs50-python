from twttr import shorten


def test():
    assert shorten("aryan") == "ryn"
    assert shorten("cs50") == "cs50"
    assert shorten("AryAn") == "ryn"
    assert shorten("test.test") == "tst.tst"