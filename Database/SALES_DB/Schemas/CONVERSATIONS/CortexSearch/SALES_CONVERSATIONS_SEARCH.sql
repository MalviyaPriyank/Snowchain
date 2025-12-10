 CREATE CORTEX SEARCH SERVICE SALES_DB.CONVERSATIONS.SALES_CONVERSATIONS_SEARCH 
        ON conversation_text 
        ATTRIBUTES sales_rep_region,customer_name,conversation_date,sales_rep_name
        WAREHOUSE = SEARCH_WH
        TARGET_LAG = '20 MINUTES'
         INITIALIZE = ON_CREATE 
 COMMENT = 'Cortex Search service for searching sales representative conversations with customers' 
 AS (SELECT conversation_text, sales_rep_region, customer_name, conversation_date, sales_rep_name FROM sales_conversations)