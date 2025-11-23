
        CREATE EXTERNAL VOLUME sales_data_volume 
        STORAGE_LOCATIONS = (
            (
                NAME = 'sales_data_location'
                STORAGE_PROVIDER = 'S3'
        
            STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::123456789012:role/snowflake-access-role'
            STORAGE_BASE_URL = 's3://my-sales-bucket/data/'
             STORAGE_AWS_EXTERNAL_ID = 'ABC123XYZ'  USE_PRIVATELINK_ENDPOINT = TRUE  ))  COMMENT = Sales_data_analytics_volume 