"Testing script. DO NOT MODIFY!"

from homework_3_code import is_all_equal

def test_is_all_equal():
    
    # Positive tests
    assert is_all_equal([42]*100_000)
    assert is_all_equal(["🐶"]*100_000)
    assert is_all_equal([{1, 2}, {2, 1}])
    assert is_all_equal([[42, 42] for _ in range(100_000)])
    
    # Negative tests
    assert not is_all_equal([1, 2, 1])
    assert not is_all_equal([1 for _ in range(10_000)] + [2] + [1 for _ in range(10_000)])
    assert not is_all_equal(["🐶", "🐱", "🐶"])
    assert not is_all_equal(["🐶" for _ in range(10_000)] + ["🐱"] + ["🐶" for _ in range(10_000)])
    assert not is_all_equal([{1}, "🐱"])
    assert not is_all_equal([{1} for _ in range(10_000)] + ["🐱"] + [{1} for _ in range(10_000)])
    assert not is_all_equal([[42, 42], [42, -1], [42, 42]])
    assert not is_all_equal([[42, 42] for _ in range(10_000)] + [[42, -1]] + [[42, 42] for _ in range(10_000)])

    return f"tests pass for {is_all_equal.__name__}"