     
        CREATE SECURITY INTEGRATION github_app_integration 
        TYPE = API_AUTHENTICATION 
        AUTH_TYPE = OAUTH2 
        ENABLED = TRUE
         OAUTH_TOKEN_ENDPOINT = 'https://api.github.com/app/installations/installation_id/access_tokens' OAUTH_CLIENT_AUTH_METHOD = 'CLIENT_SECRET_POST' OAUTH_CLIENT_ID = 'github_app_id_123456' OAUTH_CLIENT_SECRET = 'github_private_key_example' OAUTH_ACCESS_TOKEN_VALIDITY = 600