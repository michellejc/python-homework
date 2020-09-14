"Testing script. DO NOT MODIFY"

from homework_3_code import hello

def test_hello():
    assert hello() == "Hello World!"
    
    return f"tests pass for {hello.__name__}"