  
        CREATE OR REPLACE PIPE 
        commerce_dev_ing.commerce_schema.products_pipe 
         AUTO_INGEST = TRUE  COMMENT = 'Snowpipe for real-time product data ingestion'  AS COPY INTO commerce_dev_ing.commerce_schema.products FROM @commerce_dev_ing.commerce_schema.products_stage FILE_FORMAT = commerce_dev_ing.commerce_schema.commerce_csv_format PATTERN = '.*[.]csv'