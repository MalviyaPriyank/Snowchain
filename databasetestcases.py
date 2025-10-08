snowflake_database_param_test_cases = {
    # ------------------------ REQUIRED PARAMETERS ------------------------
    "name": [
        "MY_DB",                  # valid - standard
        "my_db",                  # valid - lowercase
        '"My Object"',            # valid - quoted with space
        "123DB",                  # invalid - starts with number
        "DB-TEST",                # invalid - special char without quotes
    ],

    # ------------------------ SECURE DATA SHARING ------------------------
    "provider_account.share_name": [
        "PROVIDER.ACCOUNT1.SHARE_1",  # valid - fully qualified
        "ACCOUNT1.SHARE_1",           # invalid - missing provider
        '"ORG.ACCOUNT.SHARE-TEST"',   # valid - quoted identifier
    ],

    # ------------------------ DATABASE REPLICATION ------------------------
    "AS REPLICA OF": [
        "ORG1.ACCOUNT1.PRIMARY_DB",  # valid full form
        "ORG1.ACCOUNT1.DB_TEST",     # valid alternate
        "ACCOUNT1.DB_TEST",          # invalid - missing org
        '"ORG1.ACCOUNT1.DB TEST"',   # valid - quoted with space
    ],
    "account_identifier": [
        "ORG1.ACCOUNT1",             # valid - preferred format
        "abcd1234",                  # legacy locator - discouraged but valid
        "ORG1.ACCOUNT_01",           # valid - underscore allowed
        "ORG1.ACCOUNT-01",           # invalid - special character
    ],
    "primary_db_name": [
        "PROD_DB",                   # valid
        "dev_db",                    # valid - lowercase
        '"My DB"',                   # valid quoted
        "My DB",                     # invalid - space without quotes
    ],

    # ------------------------ SNAPSHOT PARAMETERS ------------------------
    "snapshot_set": [
        "SNAPSET_001",               # valid
        "SNAP_SET_20231005",         # valid
        "",                          # invalid - empty
    ],
    "snapshot_id": [
        "12345",                     # valid numeric
        "snapshot_20231005_01",      # valid alphanumeric
        "!!SNAP",                    # invalid
    ],

    # ------------------------ LISTING PARAMETERS ------------------------
    "listing_global_name": [
        "'PUBLIC_LISTING_GLOBAL_NAME'",  # valid
        "'PRIVATE_LISTING'",             # invalid - paid listing
        "'OFFLINE_LISTING'",             # valid if offline
    ],

    # ------------------------ OPTIONAL PARAMETERS ------------------------
    "TRANSIENT": [
        True, False
    ],
    "CLONE": [
        "SRC_DB",                   # valid - basic
        '"Source DB"',              # valid quoted
        "",                         # invalid
    ],
    "AT": [
        {"TIMESTAMP": "2025-01-01 12:00:00"}, 
        {"OFFSET": "-5h"}, 
        {"STATEMENT": "01a2b3c4"}, 
        {"TIMESTAMP": "1900-01-01"}  # invalid - before creation
    ],
    "IGNORE TABLES WITH INSUFFICIENT DATA RETENTION": [
        True, False
    ],
    "IGNORE HYBRID TABLES": [
        True, False
    ],
    "DATA_RETENTION_TIME_IN_DAYS": [
        0, 1, 7, 90, 100  # last one invalid for Enterprise
    ],
    "MAX_DATA_EXTENSION_TIME_IN_DAYS": [
        1, 7, 30, 365, -1  # negative invalid
    ],
    "EXTERNAL_VOLUME": [
        "MY_EXT_VOLUME", 
        '"Volume-1"', 
        "INVALID#NAME"
    ],
    "CATALOG": [
        "ICEBERG_CATALOG", 
        "CAT_INT_01", 
        "INVALID*NAME"
    ],
    "REPLACE_INVALID_CHARACTERS": [
        True, False
    ],
    "DEFAULT_DDL_COLLATION": [
        "'en-ci'", 
        "'utf8'", 
        "'invalid_collation'"
    ],
    "LOG_LEVEL": [
        "'ERROR'", "'WARN'", "'INFO'", "'DEBUG'", "'INVALID_LEVEL'"
    ],
    "TRACE_LEVEL": [
        "'LOW'", "'MEDIUM'", "'HIGH'", "'INVALID'"
    ],
    "STORAGE_SERIALIZATION_POLICY": [
        "COMPATIBLE", "OPTIMIZED", "INVALID"
    ],
    "COMMENT": [
        "'Main production database'", 
        "'Temporary test copy'", 
        "", 
        None
    ],
    "CATALOG_SYNC": [
        "OPEN_CATALOG_INT", 
        "", 
        None
    ],
    "CATALOG_SYNC_NAMESPACE_MODE": [
        "NEST", "FLATTEN", "INVALID"
    ],
    "CATALOG_SYNC_NAMESPACE_FLATTEN_DELIMITER": [
        "-", "_", "$", " ", ""  # empty invalid when FLATTEN
    ],
    "TAG": [
        {"env": "prod"}, 
        {"owner": "data_team", "criticality": "high"}, 
        {"empty": ""}
    ],
    "WITH CONTACT": [
        {"purpose": "support"}, 
        {"purpose": ["support", "security"]}, 
        {"purpose": ""}
    ],
    "OBJECT_VISIBILITY": [
        "PRIVILEGED",
        {"organization_targets": ["all_accounts_including_external"]},
        {"organization_targets": ["account:DEV1", "organization_user_group:ANALYSTS"]},
        "INVALID_VISIBILITY"
    ],
    "ENABLE_DATA_COMPACTION": [
        True, False
    ],
}
