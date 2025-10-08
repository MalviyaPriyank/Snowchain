snowflake_storage_integration_param_test_cases = {
    # ------------------------ REQUIRED PARAMETERS ------------------------
    "name": [
        "S3_INT",                         # valid — simple uppercase
        "data_int",                       # valid — lowercase / mixed
        '"My Integration"',               # valid — quoted with space
        '"int.with.dots-01"',             # valid — quoted with special chars
        "123INT",                         # invalid — starts with digit
        "int-name",                       # invalid — hyphen without quotes
        "int name",                       # invalid — space without quotes
        "",                               # invalid — empty
        "DB.INT1",                         # invalid — fully qualified not allowed
    ],

    "TYPE": [
        "EXTERNAL_STAGE",                 # valid — required type
        "EXTERNAL",                       # invalid — not supported
        "",                               # invalid — empty
        None,                             # invalid — missing type
    ],

    # ------------------------ CLOUD PROVIDER PARAMETERS ------------------------
    "STORAGE_PROVIDER": [
        "S3", "S3CHINA", "S3GOV", "GCS", "AZURE",  # valid providers :contentReference[oaicite:1]{index=1}
        "AWS", "GOOGLE", "AZ",                     # invalid / unsupported
        "", None                                   # invalid / missing
    ],

    # AWS-specific parameters (when STORAGE_PROVIDER = S3 / S3CHINA / S3GOV)
    "STORAGE_AWS_ROLE_ARN": [
        "'arn:aws:iam::123456789012:role/MyRole'",  # valid ARN
        "arn:aws:iam::123:role/role",                # invalid — missing quotes
        "",                                          # invalid
        None,                                        # invalid / missing when required
    ],

    "STORAGE_AWS_EXTERNAL_ID": [
        "'external-id-123'",                         # valid
        "",                                          # invalid — empty literal
        None,                                        # valid — optional
    ],

    "STORAGE_AWS_OBJECT_ACL": [
        "'bucket-owner-full-control'",               # valid per docs :contentReference[oaicite:2]{index=2}
        "bucket-owner-full-control",                 # invalid — missing quotes
        "'private'",                                 # invalid — unsupported ACL type
        "", None                                     # invalid / optional
    ],

    # Azure-specific parameters (if provider = AZURE)
    "AZURE_TENANT_ID": [
        "'a123b4c5-1234-123a-a12b-1a23b45678c9'",     # valid tenant id :contentReference[oaicite:3]{index=3}
        "a123b4c5-1234-123a",                         # invalid — missing quotes
        "", None                                     # invalid / optional
    ],

    # Shared parameters
    "ENABLED": [
        True, False, "TRUE", "FALSE",                # valid boolean forms
        "yes", None                                  # invalid / missing
    ],

    "USE_PRIVATELINK_ENDPOINT": [
        True, False, "TRUE", "FALSE",                # valid
        "yes", None                                  # invalid / missing
    ],

    "STORAGE_ALLOWED_LOCATIONS": [
        ["s3://bucket/path/"],                        # valid — single
        ["s3://bucket1/path1/", "s3://bucket2/"],     # valid — multiple
        ["gcs://bucket/path/"],                       # valid for GCS provider
        ["azure://acct.blob.core.windows.net/container/path/"],  # valid Azure
        ["s3://bucket/path", "invalid-url"],          # invalid — missing slash or malformed
        [],                                           # invalid — empty list
        None,                                         # invalid / missing
    ],

    "STORAGE_BLOCKED_LOCATIONS": [
        ["s3://bucket/path/blocked/"],                # valid subset
        ["s3://bucket1/blocked/", "s3://bucket2/"],   # valid
        ["invalid://url/"],                           # invalid
        [],                                           # valid — allow full but block none
        None                                          # valid / optional
    ],

    "COMMENT": [
        "'Storage integration for S3 data'",          # valid
        "''",                                         # valid empty string
        None,                                         # valid — optional
        "DROP INTEGRATION; -- test",                  # invalid / injection
        12345,                                        # invalid — not quoted
    ],

    # ------------------------ Combined / Cross-check Cases ------------------------
    # (Not separate keys but good to test combinations)
    # e.g. Provider = S3 but missing STORAGE_AWS_ROLE_ARN → invalid
    # Provider = AZURE but missing AZURE_TENANT_ID → invalid
    # PROVIDER mismatch with allowed locations (e.g. STORAGE_PROVIDER = "GCS" but allowed location "s3://...")
}
