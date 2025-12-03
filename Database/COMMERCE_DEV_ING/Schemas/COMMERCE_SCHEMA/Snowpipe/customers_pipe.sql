  
        CREATE OR REPLACE PIPE 
        commerce_dev_ing.commerce_schema.customers_pipe 
         AUTO_INGEST = TRUE  COMMENT = 'Snowpipe for real-time customer data ingestion'  AS COPY INTO commerce_dev_ing.commerce_schema.customers FROM @commerce_dev_ing.commerce_schema.customers_stage FILE_FORMAT = commerce_dev_ing.commerce_schema.commerce_csv_format PATTERN = '.*[.]csv'