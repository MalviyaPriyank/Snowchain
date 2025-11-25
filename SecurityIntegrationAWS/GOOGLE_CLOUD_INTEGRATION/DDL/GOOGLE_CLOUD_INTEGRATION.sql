     
        CREATE SECURITY INTEGRATION google_cloud_integration 
        TYPE = API_AUTHENTICATION 
        AUTH_TYPE = OAUTH2 
        ENABLED = TRUE
         OAUTH_TOKEN_ENDPOINT = 'https://oauth2.googleapis.com/token' OAUTH_CLIENT_AUTH_METHOD = 'CLIENT_SECRET_POST' OAUTH_CLIENT_ID = 'sample_google_client_id' OAUTH_CLIENT_SECRET = 'sample_google_secret' OAUTH_ACCESS_TOKEN_VALIDITY = 3600