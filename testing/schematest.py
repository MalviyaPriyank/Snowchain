snowflake_schema_param_test_cases = {
    # ------------------------ REQUIRED PARAMETERS ------------------------
    "name": [
        "PUBLIC",                   # valid - standard
        "sales_data",               # valid - lowercase
        '"My Schema"',              # valid - quoted with space
        "123SCHEMA",                # invalid - starts with number
        "SCHEMA-TEST",              # invalid - special char without quotes
    ],

    # ------------------------ SNAPSHOT PARAMETERS ------------------------
    "snapshot_set": [
        "SCHEMA_SNAPSET_001",       # valid
        "SNAPSET_20231005",         # valid
        "",                         # invalid - empty
    ],
    "snapshot_id": [
        "10001",                    # valid numeric
        "snapshot_20231005_01",     # valid alphanumeric
        "!!SNAP",                   # invalid characters
    ],

    # ------------------------ OPTIONAL PARAMETERS ------------------------
    "TRANSIENT": [
        True, False
    ],

    "CLONE": [
        "SOURCE_SCHEMA",            # valid
        '"Source Schema"',          # valid quoted
        "",                         # invalid
    ],

    "AT": [
        {"TIMESTAMP": "2025-01-01 12:00:00"}, 
        {"OFFSET": "-2h"}, 
        {"STATEMENT": "01b3d5c7"}, 
        {"TIMESTAMP": "1900-01-01"}  # invalid - before creation
    ],

    "IGNORE TABLES WITH INSUFFICIENT DATA RETENTION": [
        True, False
    ],

    "IGNORE HYBRID TABLES": [
        True, False
    ],

    "WITH MANAGED ACCESS": [
        True, False
    ],

    "DATA_RETENTION_TIME_IN_DAYS": [
        0, 1, 7, 90, 100  # last invalid for Enterprise
    ],

    "MAX_DATA_EXTENSION_TIME_IN_DAYS": [
        1, 7, 30, 365, -1  # negative invalid
    ],

    "EXTERNAL_VOLUME": [
        "MY_EXT_VOLUME", 
        '"External-Vol1"', 
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

    "CLASSIFICATION_PROFILE": [
        "'PII_Profile'", 
        "'Finance_Profile'", 
        "'INVALID#PROFILE'"
    ],

    "COMMENT": [
        "'Operational schema for sales data'", 
        "'Temporary analytics schema'", 
        "", 
        None
    ],

    "CATALOG_SYNC": [
        "OPEN_CATALOG_INT", 
        "", 
        None
    ],

    "TAG": [
        {"env": "prod"}, 
        {"owner": "data_team", "criticality": "medium"}, 
        {"empty": ""}
    ],

    "WITH CONTACT": [
        {"purpose": "support"}, 
        {"purpose": ["security", "operations"]}, 
        {"purpose": ""}
    ],

    "OBJECT_VISIBILITY": [
        "PRIVILEGED",       # valid default
        "INVALID_VISIBILITY" # invalid
    ],

    "ENABLE_DATA_COMPACTION": [
        True, False
    ],
}
