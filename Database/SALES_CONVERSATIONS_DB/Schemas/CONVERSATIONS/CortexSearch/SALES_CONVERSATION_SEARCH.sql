 CREATE CORTEX SEARCH SERVICE SALES_CONVERSATIONS_DB.CONVERSATIONS.SALES_CONVERSATION_SEARCH 
        ON conversation_text 
        ATTRIBUTES sales_rep_region,customer_id,customer_name,product_discussed,conversation_type
        WAREHOUSE = SEARCH_WH
        TARGET_LAG = '20 MINUTES'
         INITIALIZE = ON_CREATE 
 COMMENT = 'Search service for sales conversations' 
 AS (SELECT conversation_text, sales_rep_region, customer_id, customer_name, product_discussed, conversation_type, conversation_timestamp FROM sales_conversations)