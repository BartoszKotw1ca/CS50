from twttr import shorten

def test1():
	assert shorten("asb") == "sb", "Test case 1 failed"
	assert shorten("Hello World") == "Hll Wrld", "Test case 2 failed"
	assert shorten("OpenAI") == "pn", "Test case 3 failed"
	assert shorten("BCDFGHJKLMNPQRSTVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ", "Test case 4 failed"
	assert shorten("aeiouAEIOU") == "", "Test case 5 failed"

def test2():
	assert shorten("") == "", "Test case 6 failed"  # Empty string
	assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz", "Test case 7 failed"  # Lowercase alphabet
	assert shorten("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ", "Test case 8 failed"  # Uppercase alphabet
	assert shorten("The quick brown fox jumps over the lazy dog") == "Th qck brwn fx jmps vr th lzy dg", "Test case 9 failed"  # Pangram
	assert shorten("Python Programming") == "Pythn Prgrmmng", "Test case 10 failed"  # Mixed case

def test3():
	assert shorten("1234567890") == "1234567890", "Test case 11 failed"  # Numbers only
	assert shorten("Th!s !s @ t3st str!ng.") == "Th!s !s @ t3st str!ng.", "Test case 12 failed"  # Special characters and numbers
	assert shorten("    ") == "    ", "Test case 13 failed"  # Spaces only
	assert shorten("Aeiou") == "", "Test case 14 failed"  # Vowels only in mixed case
	assert shorten("bcdfg BCDFG") == "bcdfg BCDFG", "Test case 15 failed"  # Consonants with space

