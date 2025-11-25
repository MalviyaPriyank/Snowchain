       
        CREATE SECURITY INTEGRATION azure_ad_integration 
        TYPE = API_AUTHENTICATION 
        AUTH_TYPE = OAUTH2 
        ENABLED = TRUE
         OAUTH_TOKEN_ENDPOINT = 'https://login.microsoftonline.com/tenant-id/oauth2/v2.0/token' OAUTH_CLIENT_AUTH_METHOD = 'CLIENT_SECRET_POST' OAUTH_CLIENT_ID = 'sample_azure_client_id' OAUTH_CLIENT_SECRET = 'sample_azure_secret' OAUTH_ACCESS_TOKEN_VALIDITY = 3600 OAUTH_AUTHORIZATION_ENDPOINT = 'https://login.microsoftonline.com/tenant-id/oauth2/v2.0/authorize' OAUTH_REFRESH_TOKEN_VALIDITY = 7200