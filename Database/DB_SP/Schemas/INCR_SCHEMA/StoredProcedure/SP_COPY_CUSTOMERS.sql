
        CREATE PROCEDURE 
        DB_SP.INCR_SCHEMA.SP_COPY_CUSTOMERS() 
        RETURNS VARCHAR
        LANGUAGE SQL
        AS
        $$
            BEGIN
                INSERT INTO incr_schema.customers SELECT * FROM dev_schema.customers;
            END;
        $$
        