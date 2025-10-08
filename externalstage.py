snowflake_external_stage_param_test_cases = {
    # ------------------------ IDENTIFIER ------------------------
    "name": [
        "STAGE_EXT",                  # valid
        "stage_external",             # valid
        '"External Stage"',           # valid quoted
        '"stage.ext-01"',             # valid quoted
        "123stage",                   # invalid
        "stage data",                 # invalid
        "",                           # invalid
        "DB.SCHEMA.STAGE_EXT",        # valid
        "DB.SCHEMA.SUB.STAGE",        # invalid
    ],

    # ------------------------ URL ------------------------
    "URL": [
        "'s3://mybucket/path/'",                               # valid S3
        "'s3china://bucket/path/'",                            # valid S3 China
        "'s3gov://govbucket/path/'",                           # valid S3 Gov
        "'gcs://mybucket/path/'",                              # valid GCS
        "'azure://acct.blob.core.windows.net/container/path/'", # valid Azure
        "'s3compat://bucket/path/'",                           # valid S3-compatible
        "s3://bucket/path/",                                   # invalid - missing quotes
        "",                                                    # invalid
        None,                                                  # invalid - required for external
    ],

    # ------------------------ STORAGE INTEGRATION ------------------------
    "STORAGE_INTEGRATION": [
        "MY_STORAGE_INTEGRATION",      # valid
        "storage_int_1",               # valid
        "123integration",              # invalid
        "",                            # invalid
    ],

    # ------------------------ CREDENTIALS ------------------------
    "CREDENTIALS": [
        {"AWS_KEY_ID": "key", "AWS_SECRET_KEY": "secret", "AWS_TOKEN": "token"},  # valid IAM user
        {"AWS_ROLE": "arn:aws:iam::123456789012:role/MyRole"},                   # valid IAM role
        {"AZURE_SAS_TOKEN": "sv=2022-11-02&sig=xyz"},                            # valid Azure
        {"AWS_KEY_ID": "key"},                                                   # invalid - incomplete
        {},                                                                      # invalid
    ],

    # ------------------------ ENCRYPTION ------------------------
    "ENCRYPTION": [
        {"TYPE": "AWS_SSE_S3"},                                                 # valid
        {"TYPE": "AWS_CSE", "MASTER_KEY": "abc123=="},                          # valid
        {"TYPE": "AWS_SSE_KMS", "KMS_KEY_ID": "arn:kms:key"},                   # valid
        {"TYPE": "NONE"},                                                       # valid
        {"TYPE": "GCS_SSE_KMS", "KMS_KEY_ID": "gcs-key-id"},                    # valid
        {"TYPE": "AZURE_CSE", "MASTER_KEY": "xyz456=="},                        # valid
        {"TYPE": "INVALID"},                                                    # invalid
        {"TYPE": "AWS_CSE"},                                                    # invalid - missing MASTER_KEY
    ],

    # ------------------------ AWS ACCESS POINT ARN ------------------------
    "AWS_ACCESS_POINT_ARN": [
        "'arn:aws:s3:us-east-1:123456789012:accesspoint/myap'",                 # valid
        "arn:aws:s3:::accesspoint",                                             # invalid - missing quotes
        "",                                                                     # invalid
    ],

    # ------------------------ PRIVATELINK ------------------------
    "USE_PRIVATELINK_ENDPOINT": [
        True, False, "TRUE", "FALSE",    # valid
        "yes", None                      # invalid
    ],

    # ------------------------ DIRECTORY TABLE ------------------------
    "DIRECTORY_TABLE": [
        {"ENABLE": True, "REFRESH_ON_CREATE": True, "AUTO_REFRESH": False},     # valid AWS/GCS/Azure
        {"ENABLE": False},                                                      # valid
        {"ENABLE": True, "NOTIFICATION_INTEGRATION": "NOTIF_INT"},              # valid for GCS/Azure
        {"ENABLE": True, "REFRESH_ON_CREATE": "INVALID"},                       # invalid
        {},                                                                     # valid
    ],

    # ------------------------ COMMENT ------------------------
    "COMMENT": [
        "'External stage for data lake ingestion'",     # valid
        "'Stage linked to S3 data bucket'",             # valid
        "''",                                           # valid
        None,                                           # valid
        "'DROP TABLE; -- test'",                        # invalid
        12345,                                          # invalid
    ],

    # ------------------------ TAG ------------------------
    "TAG": [
        {"env": "prod"},                                # valid
        {"project": "analytics", "team": "ml"},         # valid
        {"env": ""},                                    # invalid
        {"team@": "core"},                              # invalid
    ],
}
