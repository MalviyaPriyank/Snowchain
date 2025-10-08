snowflake_stage_param_test_cases = {
    # =========================
    # IDENTIFIER / CORE PARAMS
    # =========================
    "internal_stage_name_or_external_stage_name": [
        "STAGE_INTERNAL",             # valid - standard
        "stage_data_lake",            # valid - lowercase
        '"My Stage"',                 # valid - quoted, contains space
        '"stage.test-01"',            # valid - quoted with special chars
        "123stage",                   # invalid - starts with number
        "stage-data",                 # invalid - special char without quotes
        "stage name",                 # invalid - space without quotes
        "",                           # invalid - empty
        "DB.SCHEMA.STAGE_EXT",        # valid - fully qualified
        "DB.SCHEMA.SUB.STAGE",        # invalid - too many qualifiers
    ],

    # =========================
    # STAGE TYPE
    # =========================
    "TEMP": [
        True, False,                  # valid (TEMP/TEMPORARY)
        "TEMP", "TEMPORARY",          # valid string representation
        None,                         # valid (optional)
        "PERMANENT",                  # invalid - not supported keyword
    ],

    # =========================
    # FILE FORMAT
    # =========================
    "FILE_FORMAT": [
        {"FORMAT_NAME": "MY_CSV_FORMAT"},                      # valid - named file format
        {"TYPE": "CSV"},                                       # valid
        {"TYPE": "PARQUET"},                                   # valid
        {"TYPE": "CUSTOM"},                                    # valid
        {"TYPE": "JSON"},                                      # valid
        {"FORMAT_NAME": "F1", "TYPE": "CSV"},                  # invalid - mutually exclusive
        {"TYPE": "TXT"},                                       # invalid - unsupported type
        {},                                                    # invalid - missing keys
    ],

    # =========================
    # COMMENT
    # =========================
    "COMMENT": [
        "'Stage for raw data ingestion'",                      # valid
        "'Temporary Snowpipe stage'",                          # valid
        "''",                                                  # valid - empty
        None,                                                  # valid - optional
        "DROP TABLE; -- test",                                 # invalid - injection
        12345,                                                 # invalid - not a string literal
    ],

    # =========================
    # TAGS
    # =========================
    "TAG": [
        {"env": "dev"},                                        # valid - single tag
        {"project": "etl", "team": "data"},                    # valid - multiple tags
        {"env": ""},                                           # invalid - empty value
        {"@env": "prod"},                                      # invalid - special char in tag name
    ],

    # =========================
    # INTERNAL STAGE PARAMS
    # =========================
    "ENCRYPTION_INTERNAL": [
        {"TYPE": "SNOWFLAKE_FULL"},                            # valid
        {"TYPE": "SNOWFLAKE_SSE"},                             # valid
        {"TYPE": "INVALID_TYPE"},                              # invalid
        {},                                                    # valid - default
        {"TYPE": ""},                                          # invalid - empty
    ],

    # =========================
    # EXTERNAL STAGE PARAMS
    # =========================
    "URL": [
        "'s3://mybucket/path/'",                               # valid S3
        "'s3china://bucket/path/'",                            # valid S3 China
        "'s3gov://govbucket/path/'",                           # valid Gov
        "'gcs://mybucket/path/'",                              # valid GCS
        "'azure://acct.blob.core.windows.net/container/path/'", # valid Azure
        "'s3compat://bucket/path/'",                           # valid S3-compatible
        "s3://bucket/path/",                                   # invalid - missing quotes
        "",                                                    # invalid - empty
        None,                                                  # valid - implies internal stage
    ],

    "AWS_ACCESS_POINT_ARN": [
        "'arn:aws:s3:us-east-1:123456789012:accesspoint/myap'", # valid
        "arn:aws:s3:::accesspoint",                              # invalid - missing quotes
        "",                                                      # invalid - empty
    ],

    # =========================
    # CREDENTIALS
    # =========================
    "CREDENTIALS": [
        {"AWS_KEY_ID": "key", "AWS_SECRET_KEY": "secret", "AWS_TOKEN": "token"},  # valid IAM user
        {"AWS_ROLE": "arn:aws:iam::123456789012:role/MyRole"},                   # valid IAM role
        {"AZURE_SAS_TOKEN": "sv=2022-11-02&sig=xyz"},                            # valid Azure
        {"AWS_KEY_ID": "key"},                                                   # invalid - incomplete
        {},                                                                      # invalid - empty
    ],

    # =========================
    # STORAGE INTEGRATION
    # =========================
    "STORAGE_INTEGRATION": [
        "MY_STORAGE_INTEGRATION",          # valid
        "storage_int_1",                   # valid
        "123integration",                  # invalid - starts with number
        "",                                # invalid - empty
    ],

    # =========================
    # ENCRYPTION (External)
    # =========================
    "ENCRYPTION_EXTERNAL": [
        {"TYPE": "AWS_SSE_S3"},                                                # valid - AWS
        {"TYPE": "AWS_CSE", "MASTER_KEY": "abc123=="},                         # valid client-side
        {"TYPE": "AWS_SSE_KMS", "KMS_KEY_ID": "arn:kms:key"},                  # valid KMS
        {"TYPE": "NONE"},                                                      # valid
        {"TYPE": "GCS_SSE_KMS", "KMS_KEY_ID": "gcs-key-id"},                   # valid GCS
        {"TYPE": "AZURE_CSE", "MASTER_KEY": "xyz456=="},                       # valid Azure
        {"TYPE": "INVALID"},                                                   # invalid - unsupported
        {"TYPE": "AWS_CSE"},                                                   # invalid - missing MASTER_KEY
    ],

    "USE_PRIVATELINK_ENDPOINT": [
        True, False, "TRUE", "FALSE",       # valid
        "yes", None                         # invalid
    ],

    # =========================
    # DIRECTORY TABLE PARAMS
    # =========================
    "DIRECTORY_TABLE_INTERNAL": [
        {"ENABLE": True, "AUTO_REFRESH": False},                # valid
        {"ENABLE": False},                                      # valid - disable
        {"ENABLE": "TRUE"},                                     # valid - string literal
        {"AUTO_REFRESH": "yes"},                                # invalid - invalid string
        {},                                                     # valid - defaults apply
    ],

    "DIRECTORY_TABLE_EXTERNAL": [
        {"ENABLE": True, "REFRESH_ON_CREATE": True, "AUTO_REFRESH": False},     # valid AWS/GCS/Azure
        {"ENABLE": False},                                                      # valid
        {"ENABLE": True, "NOTIFICATION_INTEGRATION": "NOTIF_INT"},              # valid GCS/Azure only
        {"ENABLE": True, "REFRESH_ON_CREATE": "INVALID"},                       # invalid - not boolean
        {},                                                                     # valid - defaults
    ],
}
