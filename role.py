snowflake_create_role_param_test_cases = {
    # ------------------------ REQUIRED PARAMETER ------------------------
    "name": [
        "ADMIN_ROLE",                    # valid — uppercase simple
        "data_reader",                   # valid — lowercase
        '"My Role"',                      # valid — quoted with space
        '"role.with.dots-01"',            # valid — quoted, containing dot and hyphen
        "123ROLE",                       # invalid — starts with a digit
        "ROLE-NAME",                     # invalid — hyphen without quotes
        "role name",                     # invalid — unquoted space
        "",                              # invalid — empty
        "ORG.ACCOUNT.ROLE1",             # valid — fully qualified (account-level)
        "DB.SCHEMA.ROLE",                # invalid — too many dot qualifiers (namespace misuse)
    ],

    # ------------------------ OPTIONAL PARAMETERS ------------------------
    "COMMENT": [
        "'This is an admin role'",       # valid — simple quoted string
        "''",                             # valid — empty string literal
        None,                             # valid — no comment
        "DROP TABLE; -- test",            # invalid — not properly quoted / injection risk
        12345,                            # invalid — not a string literal
    ],

    "TAG": [
        {"env": "prod"},                                 # valid — single tag
        {"team": "analytics", "purpose": "read_only"},   # valid — multiple tags
        {"env": ""},                                     # invalid — empty tag value
        {"@env": "dev"},                                 # invalid — special character in tag name
        {},                                              # valid — no tags (i.e. optional)
    ],

    # ------------------------ Combined variants (for multi-parameter testing) ---------------
    # These aren’t strictly separate keys, but you might test combinations like:
    # (name, comment, tag) → e.g. ("MyRole", "'desc'", {"key":"value"}), etc.
}
