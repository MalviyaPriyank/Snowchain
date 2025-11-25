      
        CREATE SECURITY INTEGRATION servicenow_integration 
        TYPE = API_AUTHENTICATION 
        AUTH_TYPE = OAUTH2 
        ENABLED = TRUE
         OAUTH_TOKEN_ENDPOINT = 'https://myinstance.service-now.com/oauth_token.do' OAUTH_CLIENT_AUTH_METHOD = 'CLIENT_SECRET_BASIC' OAUTH_CLIENT_ID = 'sample_servicenow_client_id' OAUTH_CLIENT_SECRET = 'sample_servicenow_secret' OAUTH_ACCESS_TOKEN_VALIDITY = 3600 OAUTH_ALLOWED_SCOPES = ('api,web')