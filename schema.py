snowflake_create_schema_param_test_cases = {
    # ------------------------ REQUIRED PARAMETER ------------------------
    "name": [
        "MY_SCHEMA",                     # valid — uppercase
        "sales_data",                    # valid — lowercase
        '"My Schema"',                   # valid — quoted (space)
        '"schema.with.dots-01"',         # valid — quoted with special chars
        "123schema",                     # invalid — starts with digit
        "schema-name",                   # invalid — hyphen without quotes
        "schema name",                   # invalid — space without quotes
        "",                              # invalid — empty
        "DB.MY_SCHEMA",                  # valid — fully qualified
        "DB.SCHEMA.SUB",                 # invalid — too many qualifiers
    ],

    # ------------------------ TRANSIENT (optional) ------------------------
    "TRANSIENT": [
        True, False,                     # valid (or omitted)
        "TRANSIENT",                     # valid string form
        "PERMANENT",                     # invalid — not allowed keyword
        None,                            # valid — default (permanent)
    ],

    # ------------------------ CLONE & TIME TRAVEL ------------------------
    "CLONE": [
        "SOURCE_SCHEMA",                          # valid — clone source schema
        '"Source Schema"',                        # valid — quoted
        "",                                       # invalid — empty
    ],
    "AT | BEFORE": [
        {"TIMESTAMP": "2025-01-01 12:00:00"}, 
        {"OFFSET": "-5h"}, 
        {"STATEMENT": "01a2b3"}, 
        {"TIMESTAMP": "1900-01-01"}               # invalid — before creation point
    ],
    "IGNORE TABLES WITH INSUFFICIENT DATA RETENTION": [
        True, False
    ],
    "IGNORE HYBRID TABLES": [
        True, False
    ],

    # ------------------------ WITH MANAGED ACCESS ------------------------
    "WITH MANAGED ACCESS": [
        True, False, "TRUE", "FALSE", None
    ],

    # ------------------------ TIME TRAVEL & EXTENSION ------------------------
    "DATA_RETENTION_TIME_IN_DAYS": [
        0, 1, 7, 30, 90, 100   # last possibly invalid (exceeds enterprise max) :contentReference[oaicite:1]{index=1}
    ],
    "MAX_DATA_EXTENSION_TIME_IN_DAYS": [
        1, 7, 30, 365, -1, 0   # negative invalid, zero borderline
    ],

    # ------------------------ EXTERNAL / ICEBERG PARAMETERS ------------------------
    "EXTERNAL_VOLUME": [
        "VOL1", '"Vol-1"', "", None
    ],
    "CATALOG": [
        "ICE_CATALOG", "cat_int_01", "", None
    ],
    "REPLACE_INVALID_CHARACTERS": [
        True, False, "TRUE", "FALSE", None
    ],
    "DEFAULT_DDL_COLLATION": [
        "'en-ci'", "'utf8'", "'invalid_collation'", "", None
    ],
    "STORAGE_SERIALIZATION_POLICY": [
        "COMPATIBLE", "OPTIMIZED", "INVALID", None
    ],
    "CLASSIFICATION_PROFILE": [
        "'Profile1'", "'FinanceProf'", "", None
    ],

    # ------------------------ METADATA & TAGGING ------------------------
    "COMMENT": [
        "'Schema for sales reporting'", 
        "''", 
        None, 
        "DROP schema; -- test", 
        12345
    ],
    "CATALOG_SYNC": [
        "OPEN_CATALOG_INT", "", None
    ],
    "TAG": [
        {"env": "prod"}, 
        {"team": "analytics", "dept": "sales"}, 
        {"env": ""}, 
        {"@env": "dev"}, 
        {}
    ],
    "WITH CONTACT": [
        {"purpose": "owner"}, 
        {"purpose": ["admin", "security"]}, 
        {"purpose": ""}, 
        {}
    ],
    "OBJECT_VISIBILITY": [
        "PRIVILEGED", 
        "INVALID_VISIBILITY", 
        None
    ],
    "ENABLE_DATA_COMPACTION": [
        True, False, "TRUE", "FALSE", None
    ],

    # ------------------------ SNAPSHOT RESTORE ------------------------
    "SNAPSHOT_SET": [
        "SS_001", "snapshot_202310", "", None
    ],
    "SNAPSHOT_ID": [
        "snap123", "20231001_001", "", None
    ],
}
