 CREATE TASK ASSETSDB.DEMO.MONITOR_WAREHOUSE_CREDITS  WAREHOUSE = COMPUTE_WH  AS  MERGE INTO warehouse_credit_usage AS target
USING (
    SELECT 
        warehouse_name,
        start_time,
        end_time,
        credits_used,
        bytes_scanned,
        execution_time,
        query_type
    FROM snowflake.account_usage.warehouse_metering_history
    WHERE start_time >= dateadd(hour, -1, current_timestamp())
) AS source
ON target.warehouse_name = source.warehouse_name 
   AND target.start_time = source.start_time
WHEN NOT MATCHED THEN
    INSERT (warehouse_name, start_time, end_time, credits_used, bytes_scanned, execution_time, query_type)
    VALUES (source.warehouse_name, source.start_time, source.end_time, source.credits_used, 
            source.bytes_scanned, source.execution_time, source.query_type); 