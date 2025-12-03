   
        CREATE OR REPLACE FILE FORMAT  
        business_ops_db.operations.CSV_NEWLINE_FORMAT 
         TYPE = CSV 
 RECORD_DELIMITER = '\n' 
 COMMENT = 'File format for CSV files with newline as record delimiter' 