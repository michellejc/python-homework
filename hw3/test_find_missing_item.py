"Testing script. DO NOT MODIFY!"

from homework_3_code import find_missing_item

def test_find_missing_item():
    
    assert find_missing_item(old=[1, 2, 3, 4, 5], 
                             new=[5, 4, 3, 2, 1]) == []
    
    assert find_missing_item(old=[1, 2, 3, 4, 5], 
                             new=[1, 2,    4])    == [3, 5]

    assert find_missing_item(old=[1, 2, 3, 4], 
                             new=[   2,    4])    == [1, 3]

    assert find_missing_item(old=[1, 2, 2, 1, 1, 2, 1, 1, 2], 
                             new=[   2, 2, 1, 1, 1, 2, 2, 1]) == [1]   

    assert find_missing_item(old=[3.4, 7.8, 4.2], 
                             new=[3.4,      4.2]) == [7.8]

    assert find_missing_item(old=[1, "foo", 2, 3], 
                             new=[1,        2, 3]) == ["foo"]

    assert find_missing_item(old=["foo", 1, 2, {3, 4}, {5}], 
                             new=[       1, 2, {3, 4}     ])  == ["foo", {5}]

    assert find_missing_item(old=[1, "foo", 2, [3, 4]], 
                             new=[1,        2, [3, 4]])  == ["foo"]

    assert find_missing_item(old=[{1}, {2, 3}, {2}], 
                             new=[     {2, 3}     ])     == [{1}, {2}]

    return f"tests pass for {find_missing_item.__name__}"