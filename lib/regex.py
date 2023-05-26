import re

my_pattern = r"(It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\.)"
my_regex = re.compile(my_pattern)

def test_matches_strings():
    assert my_regex.fullmatch("It's such a lovely day today.")
    assert my_regex.fullmatch("Some weather we're having today, huh?")
    assert my_regex.fullmatch("Maybe today's just not my day.")

test_matches_strings()
