
        CREATE PROCEDURE 
        COMMERCE_DEV.COMMERCE_DATA_INCREMENTAL.SP_LOAD_INCREMENTAL_DATA() 
        RETURNS VARCHAR
        LANGUAGE SQL
        AS
        $$
            BEGIN
                BEGIN MERGE INTO COMMERCE_DEV.COMMERCE_DATA_INCREMENTAL.CUSTOMERS t USING COMMERCE_DEV.COMMERCE_DATA.CUSTOMERS s ON t.customer_id = s.customer_id WHEN NOT MATCHED THEN INSERT (customer_id, first_name, last_name, email, phone, date_joined) VALUES (s.customer_id, s.first_name, s.last_name, s.email, s.phone, s.date_joined); MERGE INTO COMMERCE_DEV.COMMERCE_DATA_INCREMENTAL.PRODUCTS t USING COMMERCE_DEV.COMMERCE_DATA.PRODUCTS s ON t.product_id = s.product_id WHEN NOT MATCHED THEN INSERT (product_id, product_name, category_id, unit_price, stock_quantity) VALUES (s.product_id, s.product_name, s.category_id, s.unit_price, s.stock_quantity); MERGE INTO COMMERCE_DEV.COMMERCE_DATA_INCREMENTAL.CATEGORIES t USING COMMERCE_DEV.COMMERCE_DATA.CATEGORIES s ON t.category_id = s.category_id WHEN NOT MATCHED THEN INSERT (category_id, category_name, description) VALUES (s.category_id, s.category_name, s.description); RETURN 'Success'; EXCEPTION WHEN OTHER THEN RETURN OBJECT_CONSTRUCT('Error', 'Failed to load incremental data: ' || SQLERRM); END;;
            END;
        $$
        