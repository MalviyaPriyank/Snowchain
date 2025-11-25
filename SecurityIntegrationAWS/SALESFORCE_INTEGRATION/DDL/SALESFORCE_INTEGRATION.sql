       
        CREATE SECURITY INTEGRATION salesforce_integration 
        TYPE = API_AUTHENTICATION 
        AUTH_TYPE = OAUTH2 
        ENABLED = TRUE
         OAUTH_TOKEN_ENDPOINT = 'https://login.salesforce.com/services/oauth2/token' OAUTH_CLIENT_AUTH_METHOD = 'CLIENT_SECRET_POST' OAUTH_CLIENT_ID = 'salesforce_consumer_key' OAUTH_CLIENT_SECRET = 'salesforce_consumer_secret' OAUTH_ACCESS_TOKEN_VALIDITY = 7200 OAUTH_AUTHORIZATION_ENDPOINT = 'https://login.salesforce.com/services/oauth2/authorize' OAUTH_REFRESH_TOKEN_VALIDITY = 86400