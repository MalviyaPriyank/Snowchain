
        CREATE EXTERNAL VOLUME azure_exvol 
        STORAGE_LOCATIONS = (
            (
                NAME = 'my-azure-northeurope'
                STORAGE_PROVIDER = 'AZURE'
        
            AZURE_TENANT_ID = 'a123b4c5-1234-123a-a12b-1a23b45678c9'
            STORAGE_BASE_URL = 'azure://exampleacct.blob.core.windows.net/my_container_northeurope/'
             ))  COMMENT = 'External volume for Azure Blob Storage in North Europe' 