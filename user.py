snowflake_create_user_param_test_cases = {
    # ------------------------ REQUIRED PARAMETERS ------------------------
    "name": [
        "user1",                          # valid — simple lowercase
        "USER_123",                       # valid — alphanumeric with underscore
        '"User One"',                    # valid — quoted with space
        '"user.with.dots-01"',           # valid — quoted with special chars
        "123user",                        # invalid — starts with digit
        "user-name",                      # invalid — hyphen without quotes
        "user name",                     # invalid — space without quotes
        "",                               # invalid — empty
        "DB.USER1",                      # invalid — fully qualified not allowed
    ],

    # ------------------------ REQUIRED PARAMETERS ------------------------
    "PASSWORD": [
        "'abc123'",                       # valid — simple password
        "'P@ssw0rd!2025'",               # valid — complex password
        "'123456'",                       # valid — numeric password
        "",                               # invalid — empty
        None,                             # invalid — missing
    ],

    # ------------------------ OPTIONAL PARAMETERS ------------------------
    "DEFAULT_ROLE": [
        "myrole",                         # valid — existing role
        '"My Role"',                     # valid — quoted role name
        "",                               # invalid — empty
        None,                             # valid — optional
        "non_existent_role",              # invalid — non-existent role
    ],

    "DEFAULT_SECONDARY_ROLES": [
        "('role1', 'role2')",             # valid — multiple roles
        "('role1')",                     # valid — single role
        "()",                            # valid — empty list
        "",                              # invalid — empty string
        None,                            # valid — optional
        "('non_existent_role')",         # invalid — non-existent role
    ],

    "MUST_CHANGE_PASSWORD": [
        True, False, "TRUE", "FALSE",     # valid boolean forms
        "yes", None                      # invalid / missing
    ],

    "COMMENT": [
        "'New user for data access'",     # valid
        "''",                             # valid empty string
        None,                             # valid — optional
        "DROP USER; -- test",             # invalid — SQL injection
        12345,                            # invalid — not quoted
    ],

    # ------------------------ SESSION PARAMETERS ------------------------
    "DEFAULT_WAREHOUSE": [
        "my_warehouse",                   # valid — existing warehouse
        '"My Warehouse"',                 # valid — quoted warehouse name
        "",                               # invalid — empty
        None,                             # valid — optional
        "non_existent_warehouse",         # invalid — non-existent warehouse
    ],

    "DEFAULT_NAMESPACE": [
        "my_database.my_schema",          # valid — existing namespace
        '"My Database"."My Schema"',     # valid — quoted namespace
        "",                               # invalid — empty
        None,                             # valid — optional
        "non_existent_database.non_existent_schema",  # invalid — non-existent namespace
    ],

    "DEFAULT_ROLE": [
        "myrole",                         # valid — existing role
        '"My Role"',                     # valid — quoted role name
        "",                               # invalid — empty
        None,                             # valid — optional
        "non_existent_role",              # invalid — non-existent role
    ],

    "DEFAULT_SECONDARY_ROLES": [
        "('role1', 'role2')",             # valid — multiple roles
        "('role1')",                     # valid — single role
        "()",                            # valid — empty list
        "",                              # invalid — empty string
        None,                            # valid — optional
        "('non_existent_role')",         # invalid — non-existent role
    ],

    "MUST_CHANGE_PASSWORD": [
        True, False, "TRUE", "FALSE",     # valid boolean forms
        "yes", None                      # invalid / missing
    ],

    "COMMENT": [
        "'New user for data access'",     # valid
        "''",                             # valid empty string
        None,                             # valid — optional
        "DROP USER; -- test",             # invalid — SQL injection
        12345,                            # invalid — not quoted
    ],
}
