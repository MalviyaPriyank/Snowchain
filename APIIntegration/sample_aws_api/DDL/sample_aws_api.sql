   
        CREATE API INTEGRATION 
        sample_aws_api
        API_PROVIDER = aws_api_gateway
        
            API_AWS_ROLE_ARN = 'arn:aws:iam::123456789012:role/sample-api-role'
             API_ALLOWED_PREFIXES = ('https://api.execute-api.us-west-2.amazonaws.com/prod/')  ENABLED = FALSE  COMMENT = 'Sample AWS API Integration - Disabled' 