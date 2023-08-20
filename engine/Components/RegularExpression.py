import re


def validate_input(input_string):
	# pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$|[\^v!<>-]"
	# pattern = r"^(?:[a-zA-Z_]\d*|[a-zA-Z])$|[\^v!<>-]"
	# pattern = r"^(?:[a-zA-Z][a-zA-Z_]*\d*|[a-zA-Z])$|[\^v!<>-]"
	pattern = r"^(?:[a-zA-Z](?:_\d+)?|[a-zA-Z])$|[\^v!<>-]"
	return re.fullmatch(pattern, input_string) is not None


# Test cases
test_cases = [
	"^",
	"v",
	"P",
	"P_1",
	"P_2",
	"a",
	"a_123",
	"123",
	"@",
	"#",
	"%",
	"A",
	"B_42",
	"C_",  # questionable
	"P^Q",
	"PvQ",
	"P->Q",
	"P<->Q",
	"R_10",
	"X-Y",
	"Z_99",
	"0",
	"5",
	"P@Q",
	"abc",  # No
	"def_",
	"_xyz",
	"<",
	">",
	"R-5",
	"S^6",
	"T_7",
]
