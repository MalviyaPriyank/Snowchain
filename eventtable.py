snowflake_event_table_param_test_cases = {
    # ------------------------ REQUIRED PARAMETERS ------------------------
    "name": [
        "EVENT_LOGS",                     # valid - uppercase, standard
        "user_events",                    # valid - lowercase, standard
        '"Event Table"',                  # valid - quoted, contains space
        '"event.table.logs"',             # valid - quoted, contains dots
        "123EVENT",                       # invalid - starts with a number
        "EVENT-TABLE",                    # invalid - special char without quotes
        "event table",                    # invalid - space without quotes
        '"Event.Table-01"',               # valid - quoted with special chars
        "PUBLIC.EVENTS",                  # valid - schema qualified
        "DB.SCHEMA.EVENTS.TABLE",         # invalid - too many qualifiers
        "",                               # invalid - empty
    ],

    # ------------------------ CLONE PARAMETERS ------------------------
    "source_table": [
        "PUBLIC.SOURCE_EVENTS",           # valid - fully qualified
        "SOURCE_EVENTS",                  # valid - same schema reference
        '"Source Events"',                # valid - quoted identifier
        "SOURCE-EVENTS",                  # invalid - unquoted special char
        "",                               # invalid - empty
    ],

    # ------------------------ OPTIONAL PARAMETERS ------------------------
    "CLUSTER BY": [
        ["event_type"],                   # valid single column
        ["event_date", "user_id"],        # valid multiple columns
        ["UPPER(event_type)"],            # valid expression
        ["123col"],                       # invalid - starts with number
        [""],                             # invalid - empty column name
    ],

    "DATA_RETENTION_TIME_IN_DAYS": [
        0, 1, 7, 30, 90,  # valid (depends on edition)
        100,               # invalid - exceeds enterprise limit
        -1,                # invalid - negative
        "abc"              # invalid - non-integer
    ],

    "MAX_DATA_EXTENSION_TIME_IN_DAYS": [
        1, 7, 30, 365,     # valid
        0,                 # valid but uncommon
        -10,               # invalid - negative
        "ten"              # invalid - non-integer
    ],

    "CHANGE_TRACKING": [
        True, False,        # valid
        "TRUE", "FALSE",    # valid string representation
        "yes",              # invalid
        None                # invalid (must be explicit)
    ],

    "DEFAULT_DDL_COLLATION": [
        "'en-ci'",          # valid collation
        "'utf8'",           # valid
        "'invalid_collation'", # invalid
        "",                 # invalid
    ],

    "COPY GRANTS": [
        True, False          # valid flag
    ],

    "ROW ACCESS POLICY": [
        {"policy_name": "ROW_ACCESS_POLICY_1", "columns": ["user_id"]},                   # valid single col
        {"policy_name": "POLICY_FINANCE", "columns": ["department", "region"]},           # valid multiple
        {"policy_name": "POLICY-1", "columns": ["id"]},                                   # invalid - special char
        {"policy_name": "", "columns": []},                                               # invalid - empty
    ],

    "COMMENT": [
        "'Tracks user interactions across platform'",   # valid
        "'Temporary event audit table'",                # valid
        "''",                                           # valid but empty
        None,                                           # valid - no comment
        "'DROP TABLE; -- injection test'",              # invalid - SQL injection risk
        "12345",                                        # invalid - not quoted string
    ],

    "TAG": [
        {"env": "prod"},                                # valid single tag
        {"owner": "data_team", "type": "event"},        # valid multiple tags
        {"empty": ""},                                  # invalid - empty value
        {"tool": "ETL_PIPELINE#1"},                     # invalid - special char
    ],

    "WITH CONTACT": [
        {"purpose": "support"},                         # valid
        {"purpose": ["security", "monitoring"]},        # valid multiple
        {"purpose": ""},                                # invalid empty
    ],
}
