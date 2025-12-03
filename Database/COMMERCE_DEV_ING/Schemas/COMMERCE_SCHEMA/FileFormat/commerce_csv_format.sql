       
        CREATE OR REPLACE FILE FORMAT  
        commerce_dev_ing.commerce_schema.commerce_csv_format 
         TYPE = CSV 
 COMPRESSION = AUTO 
 RECORD_DELIMITER = '\n' 
 FIELD_DELIMITER = ',' 
 SKIP_HEADER = 1  EMPTY_FIELD_AS_NULL = TRUE  COMMENT = 'File format for commerce data CSV files' 