"Testing script. DO NOT MODIFY!"

from homework_3_code import is_strictly_increasing

def test_is_strictly_increasing():
    
    # Positive tests
    assert is_strictly_increasing([1, 2, 3])
    assert is_strictly_increasing([3.1, 3.2, 3.3])

    # Negative tests
    assert not is_strictly_increasing([1, 1, 1])       # All equal
    assert not is_strictly_increasing([3.3, 3.2, 3.1]) # Decreasing
    
    return f"tests pass for {is_strictly_increasing.__name__}"