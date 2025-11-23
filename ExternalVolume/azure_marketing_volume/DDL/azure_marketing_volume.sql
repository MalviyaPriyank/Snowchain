
        CREATE EXTERNAL VOLUME azure_marketing_volume 
        STORAGE_LOCATIONS = (
            (
                NAME = 'marketing_data_location'
                STORAGE_PROVIDER = 'AZURE'
        
            AZURE_TENANT_ID = '12345678-1234-1234-1234-123456789012'
            STORAGE_BASE_URL = 'azure://marketing-container.blob.core.windows.net/data/'
             ))  COMMENT = Marketing_data_azure_volume 