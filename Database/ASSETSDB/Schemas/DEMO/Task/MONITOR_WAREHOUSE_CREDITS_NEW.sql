 CREATE TASK ASSETSDB.DEMO.MONITOR_WAREHOUSE_CREDITS_NEW  WAREHOUSE = COMPUTE_WH  AS  INSERT INTO warehouse_credit_usage (
    warehouse_name,
    start_time,
    end_time,
    credits_used,
    bytes_scanned,
    execution_time,
    query_type
)
SELECT 
    warehouse_name,
    start_time,
    end_time,
    credits_used,
    bytes_scanned,
    execution_time,
    query_type
FROM snowflake.account_usage.warehouse_metering_history
WHERE start_time >= dateadd(hour, -1, current_timestamp()); 