snowflake_create_warehouse_param_test_cases = {
    # ------------------------ REQUIRED PARAMETERS ------------------------
    "name": [
        "my_warehouse",                    # valid — simple lowercase
        "MY_WAREHOUSE",                    # valid — uppercase
        '"My Warehouse"',                  # valid — quoted with space
        '"warehouse.with.dots-01"',        # valid — quoted with special chars
        "123warehouse",                     # invalid — starts with digit
        "warehouse-name",                   # invalid — hyphen without quotes
        "warehouse name",                   # invalid — space without quotes
        "",                                 # invalid — empty
        "DB.WAREHOUSE1",                   # invalid — fully qualified not allowed
    ],

    # ------------------------ WAREHOUSE TYPE ------------------------
    "WAREHOUSE_TYPE": [
        "STANDARD",                         # valid — standard warehouse
        "'SNOWPARK-OPTIMIZED'",             # valid — Snowpark-optimized warehouse
        "",                                 # invalid — empty
        "non_existent_type",                # invalid — non-existent type
    ],

    # ------------------------ WAREHOUSE SIZE ------------------------
    "WAREHOUSE_SIZE": [
        "XSMALL", "SMALL", "MEDIUM", "LARGE", "XLARGE", "XXLARGE", "XXXLARGE",  # valid sizes
        "X4LARGE", "X5LARGE", "X6LARGE",                                          # valid sizes
        "",                                 # invalid — empty
        "EXTRA_LARGE",                      # invalid — non-existent size
    ],

    # ------------------------ RESOURCE CONSTRAINT ------------------------
    "RESOURCE_CONSTRAINT": [
        "STANDARD_GEN_1", "STANDARD_GEN_2", "MEMORY_1X", "MEMORY_1X_x86", "MEMORY_16X", "MEMORY_16X_x86", "MEMORY_64X", "MEMORY_64X_x86",  # valid constraints
        "",                                 # invalid — empty
        "INVALID_CONSTRAINT",               # invalid — non-existent constraint
    ],

    # ------------------------ SCALING POLICY ------------------------
    "SCALING_POLICY": [
        "STANDARD",                         # valid — standard scaling
        "ECONOMY",                          # valid — economy scaling
        "",                                 # invalid — empty
        "non_existent_policy",              # invalid — non-existent policy
    ],

    # ------------------------ AUTO SUSPEND ------------------------
    "AUTO_SUSPEND": [
        "10", "60", "600", "NULL",          # valid — numeric or NULL
        "",                                 # invalid — empty
        "-1",                               # invalid — negative value
        "non_numeric",                      # invalid — non-numeric
    ],

    # ------------------------ AUTO RESUME ------------------------
    "AUTO_RESUME": [
        "TRUE", "FALSE", "NULL",            # valid boolean or NULL
        "",                                 # invalid — empty
        "non_boolean",                      # invalid — non-boolean
    ],

    # ------------------------ INITIALLY SUSPENDED ------------------------
    "INITIALLY_SUSPENDED": [
        "TRUE", "FALSE",                    # valid boolean
        "",                                 # invalid — empty
        "non_boolean",                      # invalid — non-boolean
    ],

    # ------------------------ RESOURCE MONITOR ------------------------
    "RESOURCE_MONITOR": [
        "my_monitor",                       # valid — existing resource monitor
        '"My Monitor"',                    # valid — quoted monitor name
        "",                                 # invalid — empty
        "non_existent_monitor",             # invalid — non-existent monitor
    ],

    # ------------------------ COMMENT ------------------------
    "COMMENT": [
        "'My test warehouse'",             # valid — quoted string
        "''",                              # valid — empty string
        None,                              # valid — optional
        "DROP WAREHOUSE; -- test",          # invalid — SQL injection
        12345,                             # invalid — not quoted
    ],

    # ------------------------ ENABLE QUERY ACCELERATION ------------------------
    "ENABLE_QUERY_ACCELERATION": [
        "TRUE", "FALSE", "NULL",            # valid boolean or NULL
        "",                                 # invalid — empty
        "non_boolean",                      # invalid — non-boolean
    ],

    # ------------------------ QUERY ACCELERATION MAX SCALE FACTOR ------------------------
    "QUERY_ACCELERATION_MAX_SCALE_FACTOR": [
        "1", "2", "4", "8", "16",           # valid scale factors
        "",                                 # invalid — empty
        "-1",                               # invalid — negative value
        "non_numeric",                      # invalid — non-numeric
    ],

    # ------------------------ MAX CONCURRENCY LEVEL ------------------------
    "MAX_CONCURRENCY_LEVEL": [
        "1", "5", "10", "50", "100",        # valid concurrency levels
        "",                                 # invalid — empty
        "-1",                               # invalid — negative value
        "non_numeric",                      # invalid — non-numeric
    ],

    # ------------------------ STATEMENT QUEUED TIMEOUT ------------------------
    "STATEMENT_QUEUED_TIMEOUT_IN_SECONDS": [
        "60", "300", "600", "1800",         # valid timeout values
        "",                                 # invalid — empty
        "-1",                               # invalid — negative value
        "non_numeric",                      # invalid — non-numeric
    ],

    # ------------------------ STATEMENT TIMEOUT ------------------------
    "STATEMENT_TIMEOUT_IN_SECONDS": [
        "60", "300", "600", "1800",         # valid timeout values
        "",                                 # invalid — empty
        "-1",                               # invalid — negative value
        "non_numeric",                      # invalid — non-numeric
    ],
}
