  
        CREATE OR REPLACE PIPE 
        commerce_dev_ing.commerce_schema.categories_pipe 
         AUTO_INGEST = TRUE  COMMENT = 'Snowpipe for real-time category data ingestion'  AS COPY INTO commerce_dev_ing.commerce_schema.categories FROM @commerce_dev_ing.commerce_schema.categories_stage FILE_FORMAT = commerce_dev_ing.commerce_schema.commerce_csv_format PATTERN = '.*[.]csv'