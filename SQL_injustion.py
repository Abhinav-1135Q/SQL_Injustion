import re

SQL_PATTENRN = [
    r"(\%27)|(\')|(\-\-)|(\%23)|(#)",  # ' or -- or #
    r"(/%22)|(\")|(\%3D)|(=)",         # " or =
    r"(\bOR\b|\bAND\b).*(=)",          # OR or AND followed by =
    r"UNION(\s+ALL)?\s+SELECT",        # UNION SELECT or UNION ALL SELECT
    r"INSERT\s+INTO",                  # INSERT
    r"DROP\s+TABLE",                   # DROP TABLE
    r"UPDATE\s+\w+\s+SET",             # UPDATE SET
    r"EXEC(\s+|\()",                   # EXEC or EXEC(
    r"INFORMATION_SCHEMA",             # Metadat
]

def detect_sql(input_string: str) -> bool: 
    for pattern in SQL_PATTENRN:
        if re.search(pattern, input_string, re.IGNORECASE):
            return True
    return False

test_inputs = [
    # Enter normal inputs
]

for inp in test_inputs:
    if detect_sql(inp):
        print(f"[!] SQL Injection detected: {inp}")
    else:
        print(f"[OK] safe input: {inp}")