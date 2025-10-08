snowflake_create_task_param_test_cases = {
    # ------------------------ REQUIRED PARAMETERS ------------------------
    "name": [
        "DAILY_ETL",                      # valid — simple uppercase
        "etl_task",                       # valid — lowercase
        '"My Task"',                      # valid — quoted with space
        '"task.with.dots-01"',            # valid — quoted with special chars
        "123task",                        # invalid — starts with digit
        "task-name",                      # invalid — hyphen without quotes
        "task name",                      # invalid — space without quotes
        "",                               # invalid — empty
        "DB.TASK1",                      # invalid — fully qualified not allowed
    ],

    # ------------------------ TASK DEFINITIONS ------------------------
    "sql": [
        "SELECT CURRENT_TIMESTAMP;",       # valid — simple SQL
        "CALL my_procedure();",            # valid — stored procedure call
        "SELECT * FROM my_table;",         # valid — select statement
        "INSERT INTO my_table VALUES (1);", # valid — insert statement
        "",                               # invalid — empty SQL
        "DROP TABLE my_table;",            # invalid — DDL statement
        "SELECT * FROM non_existent_table;", # invalid — references non-existent table
    ],

    # ------------------------ SCHEDULE OPTIONS ------------------------
    "SCHEDULE": [
        "'5 MINUTES'",                    # valid — interval
        "'1 HOUR'",                       # valid — interval
        "'USING CRON 0 * * * * UTC'",     # valid — cron expression
        "'USING CRON 0 0 1 * * UTC'",     # valid — cron expression
        "",                               # invalid — empty
        "USING CRON 0 0 1 * * UTC",       # invalid — missing quotes
        "1 HOUR",                         # invalid — missing quotes
    ],

    # ------------------------ WAREHOUSE OPTIONS ------------------------
    "WAREHOUSE": [
        "MY_WAREHOUSE",                   # valid — existing warehouse
        '"My Warehouse"',                 # valid — quoted name
        "",                               # invalid — empty
        "NON_EXISTENT_WAREHOUSE",         # invalid — non-existent warehouse
    ],

    "USER_TASK_MANAGED_INITIAL_WAREHOUSE_SIZE": [
        "XSMALL", "SMALL", "MEDIUM", "LARGE", "XLARGE", "XXLARGE",  # valid sizes
        "",                                                       # invalid — empty
        "EXTRA_LARGE",                                             # invalid — non-existent size
    ],

    # ------------------------ EXECUTION CONTROL ------------------------
    "ALLOW_OVERLAPPING_EXECUTION": [
        True, False, "TRUE", "FALSE",  # valid boolean forms
        "yes", None                   # invalid / missing
    ],

    "USER_TASK_TIMEOUT_MS": [
        10000, 60000, 3600000, 86400000,  # valid — milliseconds
        -1, 0, "10000", None              # invalid — negative, zero, string, missing
    ],

    "SUSPEND_TASK_AFTER_NUM_FAILURES": [
        0, 1, 3, 5, 10,  # valid — number of failures
        -1, "5", None    # invalid — negative, string, missing
    ],

    "COMMENT": [
        "'Daily ETL task'",               # valid
        "''",                             # valid empty string
        None,                             # valid — optional
        "DROP TASK; -- test",             # invalid — SQL injection
        12345,                            # invalid — not quoted
    ],

    # ------------------------ ERROR HANDLING ------------------------
    "ERROR_INTEGRATION": [
        "my_error_integration",           # valid — existing integration
        '"My Error Integration"',         # valid — quoted name
        "",                               # invalid — empty
        "NON_EXISTENT_INTEGRATION",       # invalid — non-existent integration
    ],

    "SUCCESS_INTEGRATION": [
        "my_success_integration",         # valid — existing integration
        '"My Success Integration"',       # valid — quoted name
        "",                               # invalid — empty
        "NON_EXISTENT_INTEGRATION",       # invalid — non-existent integration
    ],

    # ------------------------ LOGGING OPTIONS ------------------------
    "LOG_LEVEL": [
        "'TRACE'", "'DEBUG'", "'INFO'", "'WARN'", "'ERROR'", "'FATAL'",  # valid log levels
        "", None,                   # invalid — empty, missing
        "'INVALID'",                # invalid — non-existent level
    ],

    # ------------------------ RETRY AND FINALIZATION ------------------------
    "TASK_AUTO_RETRY_ATTEMPTS": [
        0, 1, 3, 5, 10,  # valid — number of retry attempts
        -1, "5", None    # invalid — negative, string, missing
    ],

    "FINALIZE": [
        "'COMMIT'", "'ROLLBACK'", "'ABORT'", "'NONE'",  # valid finalize options
        "", None,                                       # invalid — empty, missing
        "'INVALID'",                                    # invalid — non-existent option
    ],

    # ------------------------ DEPENDENCIES AND CONDITIONS ------------------------
    "AFTER": [
        "task1", "task2", "task3",  # valid — existing tasks
        "", None,                   # invalid — empty, missing
        "non_existent_task",        # invalid — non-existent task
    ],

    "EXECUTE AS USER": [
        "user1", "user2", "user3",  # valid — existing users
        "", None,                   # invalid — empty, missing
        "non_existent_user",        # invalid — non-existent user
    ],

    "WHEN": [
        "TRUE", "FALSE",            # valid boolean expressions
        "CURRENT_TIMESTAMP > '2025-01-01'",  # valid SQL expression
        "", None,                   # invalid — empty, missing
        "INVALID_EXPRESSION",       # invalid — non-existent expression
    ],
}
