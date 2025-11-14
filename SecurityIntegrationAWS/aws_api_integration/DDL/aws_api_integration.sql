 
        CREATE SECURITY INTEGRATION aws_api_integration 
        TYPE = API_AUTHENTICATION 
        AUTH_TYPE = AWS_IAM 
        AWS_ROLE_ARN = 'arn:aws:iam::123456789012:role/MyAppExecutionRole' 
        ENABLED = FALSE
         COMMENT = 'NONE' 