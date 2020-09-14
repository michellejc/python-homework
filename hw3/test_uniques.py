"Testing script. DO NOT MODIFY!"

from homework_3_code import uniques

def test_uniques():

    assert uniques(["🐅", "🐅", "🐅", "🐅"]) == ["🐅"]
    assert uniques(["🐅", "🤴", "🤴", "🐅", "🐅", "🤠", "🤴", "🐅"]) == ["🐅", "🤴", "🤠"]
    assert uniques([{1}, {2, 1}, {1, 2}, {1}, {1, 1}]) == [{1}, {1, 2}]
    
    return f"tests pass for {uniques.__name__}"