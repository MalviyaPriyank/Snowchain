
        CREATE EXTERNAL VOLUME secure_finance_volume 
        STORAGE_LOCATIONS = (
            (
                NAME = 'finance_data_location'
                STORAGE_PROVIDER = 'S3'
        
            STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::123456789012:role/snowflake-finance-role'
            STORAGE_BASE_URL = 's3://finance-secure-bucket/'
             ENCRYPTION = ( TYPE = 'AWS_SSE_KMS'  KMS_KEY_ID = 'arn:aws:kms:us-west-2:123456789012:key/abcd1234-ab12-cd34-ef56-abcdef123456' )  ))  COMMENT = Encrypted_finance_data_volume 