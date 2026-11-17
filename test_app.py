from app import hello_world, welcome_message


def test_hello_world():
    assert hello_world() == "Hello, DevOps!"


def test_hello_world_returns_string():
    assert isinstance(hello_world(), str)


def test_welcome_message_hemang():
    assert welcome_message("Hemang") == "Welcome to DevOps, Hemang!"


def test_welcome_message_saransh():
    assert welcome_message("Saransh") == "Welcome to DevOps, Saransh!"
