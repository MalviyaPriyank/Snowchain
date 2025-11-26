
        CREATE PROCEDURE 
        DB_SP.INCR_SCHEMA.SP_COPY_CUSTOMERS() 
        RETURNS VARCHAR
        LANGUAGE SQL
        AS
        $$
            BEGIN
                BEGIN INSERT INTO incr_schema.customers SELECT * FROM dev_schema.customers; RETURN 'Records copied successfully from dev_schema.customers to incr_schema.customers'; END;
            END;
        $$
        