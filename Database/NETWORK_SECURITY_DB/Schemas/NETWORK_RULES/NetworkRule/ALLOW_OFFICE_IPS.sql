 
        CREATE NETWORK RULE  
        NETWORK_SECURITY_DB.NETWORK_RULES.ALLOW_OFFICE_IPS 
        TYPE = IPV4 
        VALUE_LIST = ('192.168.1.0/24','10.0.0.0/16') 
        MODE = INGRESS
         COMMENT = 'Network rule to allow office IP addresses' 