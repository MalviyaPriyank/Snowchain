 CREATE CORTEX SEARCH SERVICE SALES_CONVERSATIONS_DB.CONVERSATIONS.SALES_CONVERSATIONS_SEARCH 
        ON conversation_text 
        ATTRIBUTES rep_id,cust_id,rep_name,customer_name
        WAREHOUSE = COMPUTE_WH
        TARGET_LAG = '5 MINUTES'
         INITIALIZE = ON_CREATE  COMMENT = 'Cortex Search service for natural language search on sales conversations' AS (SELECT conversation_text, rep_id, cust_id, rep_name, customer_name FROM SALES_CONVERSATIONS)