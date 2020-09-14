"Testing script. DO NOT MODIFY!"

from homework_3_code import is_valid

def test_is_valid():
    
    pairs = ["()", "[]", "{}", "⦅⦆", "〚〛", "⦃⦄", "『』", "〖〗", "〘〙", "⟦⟧",  "⟨⟩",  "⟪⟫",  "⟮⟯", "⟬⟭", "⌈⌉", "⌊⌋", "⦇⦈", "⦉⦊"]
    
    # Positive tests
    assert is_valid("".join(pairs))          # Together is valid
    assert is_valid("{[]}")                  # Nesting is valid
    assert is_valid("{⦉⦅⦆⦊}")                 # Deeper nesting is valid
    assert is_valid("<[((({⦉⦅{⦉⦅[]⦆⦊}⦆⦊})))]>") # Deeperer nesting is valid
    assert is_valid("🦄")                    # A unicorn is valid
    assert is_valid(" ⟦ 🦄 ( 🦄 ) 🦄 ⟧ ")    # A blessing of unicorns is valid  
    
    # Negative tests
    assert not is_valid("(")      # Just left is not valid
    assert not is_valid("⦇")      # Just left is not valid
    assert not is_valid("⟫")      # Just right is not valid
    assert not is_valid("(]")     # Mismatched pair is not valid
    assert not is_valid("⦉[⦊]")    # Interleaved pair is not valid

    return f"tests pass for {is_valid.__name__}"