snowflake_db_role_param_test_cases = {
    # ------------------------ REQUIRED PARAMETERS ------------------------
    "name": [
        "DATA_ENGINEER_ROLE",            # valid - uppercase, standard identifier
        "finance_admin",                 # valid - lowercase, standard identifier
        '"My Role"',                     # valid - quoted, contains space
        '"Role.With.Dot"',               # valid - quoted, special char allowed inside quotes
        "123ROLE",                       # invalid - starts with a number
        "ROLE-ADMIN",                    # invalid - special char without quotes
        "data engineer",                 # invalid - space without quotes
        '"Data Engineer"',               # valid quoted identifier with space
        "PROD_DB.DATA_ENG_ROLE",         # valid fully qualified
        "INVALID.DB.ROLE.NAME",          # invalid - too many qualifiers
        "",                              # invalid - empty
    ],

    # ------------------------ OPTIONAL PARAMETERS ------------------------
    "COMMENT": [
        "'Primary role for data engineering team'",  # valid comment
        "'Handles staging data load permissions'",   # valid
        "''",                                        # valid but empty string
        None,                                        # valid - means no comment
        "'DROP TABLE; -- injection test'",           # invalid / potential SQL injection
        "12345",                                     # invalid - not quoted string
    ],
}
