CREATE CORTEX SEARCH SERVICE cortex_search_db.search_schema.sales_call_notes_search 
        ON call_notes 
        ATTRIBUTES rep_id,customer_id
        WAREHOUSE = cortex_search_wh
        TARGET_LAG = '5 MINUTES'
         COMMENT = 'Cortex Search service for searching sales call notes with filtering capability on rep_id and customer_id' AS (SELECT call_notes, rep_id, customer_id FROM sales_call_notes)