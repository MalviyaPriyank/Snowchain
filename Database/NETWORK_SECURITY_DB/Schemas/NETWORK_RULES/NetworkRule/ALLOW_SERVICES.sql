 
        CREATE NETWORK RULE  
        NETWORK_SECURITY_DB.NETWORK_RULES.ALLOW_SERVICES 
        TYPE = HOST_PORT 
        VALUE_LIST = ('example1.com:443','example2.com:8080') 
        MODE = EGRESS
         COMMENT = 'Network rule to allow specific host and port combinations' 