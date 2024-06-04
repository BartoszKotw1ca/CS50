from plates import is_valid

def test_length():
    assert is_valid("A") == False, "Test failed: A"
    assert is_valid("AB") == True, "Test failed: AB"
    assert is_valid("ABCDEF") == True, "Test failed: ABCDEF"
    assert is_valid("ABCDEFG") == False, "Test failed: ABCDEFG"

def test_start_with_letters():
    assert is_valid("A1") == False, "Test failed: A1"
    assert is_valid("1A") == False, "Test failed: 1A"
    assert is_valid("AB1") == True, "Test failed: AB1"

def test_alphanumeric():
    assert is_valid("AB1234") == True, "Test failed: AB1234"
    assert is_valid("AB12@4") == False, "Test failed: AB12@4"

def test_no_leading_zero():
    assert is_valid("AB0123") == False, "Test failed: AB0123"
    assert is_valid("AB123") == True, "Test failed: AB123"

def test_number_placement():
    assert is_valid("AB12CD") == False, "Test failed: AB12CD"
    assert is_valid("ABCD12") == True, "Test failed: ABCD12"
    assert is_valid("AB1234") == True, "Test failed: AB1234"
    assert is_valid("ABCD1") == True, "Test failed: ABCD1"
    assert is_valid("ABC12D") == False, "Test failed: ABC12D"

def test_all():
    test_length()
    test_start_with_letters()
    test_alphanumeric()
    test_no_leading_zero()
    test_number_placement()
    print("All tests passed.")

if __name__ == "__main__":
    test_all()
