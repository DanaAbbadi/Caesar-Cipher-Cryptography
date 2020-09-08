from caesar_cipher.caesar_cipher_cryp import *


def test_encrypt():
    msg = 'I have a cat'
    actual = encrypt(msg,7)
    expected = 'p ohcl h jha'
    assert actual == expected

def test_encrypt_all_capital():
    msg = 'I HAVE A CAT'
    actual = encrypt(msg,7)
    expected = 'p ohcl h jha'
    assert actual == expected

def test_encrypt_punctuation_marks():
    msg = 'I, HAVE! #A *CAT'
    actual = encrypt(msg,7)
    expected = 'p, ohcl! #h *jha'
    assert actual == expected

def test_decrypt():
    msg = 'p ohcl h jha'
    actual = decrypt(msg,7)
    expected = 'i have a cat'
    assert actual == expected

def test_breaker():
    msg = 'toik cuxq'
    actual = cipher_breaker(msg)
    expected = 'nice work'
    assert actual == expected