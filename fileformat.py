snowflake_file_format_param_test_cases = {
    # ------------------------ REQUIRED PARAMETER ------------------------
    "name": [
        "CSV_FMT",                            # valid standard identifier
        "jsonFormat1",                        # valid lowercase/mixed
        '"My File Format"',                   # valid quoted (spaces)
        '"fmt.with.dots-01"',                 # valid quoted with special chars
        "123fmt",                             # invalid — starts with number
        "fmt-name",                           # invalid — hyphen without quotes
        "fmt name",                           # invalid — space without quotes
        "",                                   # invalid — empty
        "DB.SCHEMA.FMT1",                     # valid fully qualified
        "DB.SCHEMA.SUB.FMT",                  # invalid — too many qualifiers
    ],

    # ------------------------ TEMP / VOLATILE / TEMPORARY ------------------------
    "lifetime": [
        None,                                 # default (permanent)
        "TEMP", "TEMPORARY",                  # valid
        "VOLATILE",                           # valid
        "PERMANENT",                          # invalid (not allowed)
    ],

    # ------------------------ TYPE = format type ------------------------
    "TYPE": [
        "CSV", "JSON", "AVRO", "ORC", "PARQUET", "XML", "CUSTOM",  # valid types :contentReference[oaicite:1]{index=1}
        "TXT", "UNKNOWN",                                            # invalid types
        "",                                                          # invalid empty
        None,                                                        # valid — if omitted default = CSV :contentReference[oaicite:2]{index=2}
    ],

    # ------------------------ COMMENT ------------------------
    "COMMENT": [
        "'File format for ingest CSV'",        # valid
        "''",                                   # valid empty
        None,                                   # valid (no comment)
        "DROP TABLE; -- injection",             # invalid / unsafe
        12345,                                  # invalid — not quoted string
    ],

    # ------------------------ formatTypeOptions: CSV ------------------------
    # (These options only valid if TYPE = CSV)
    "CSV_OPTIONS": {
        "COMPRESSION": [
            "AUTO", "GZIP", "BZ2", "BROTLI", "ZSTD", "DEFLATE", "RAW_DEFLATE", "NONE",  # valid :contentReference[oaicite:3]{index=3}
            "ZIP", "", None, "INVALID"                                                  # invalid
        ],
        "RECORD_DELIMITER": [
            "\\n", "\\r\\n", "NONE", "0x0A", "\\x0A", "||", "", None, "abcd"             # valid/invalid variants
        ],
        "FIELD_DELIMITER": [
            ",", "\t", "|", "NONE", "0x7C", "", None, "||"                               # valid/invalid
        ],
        "MULTI_LINE": [
            True, False, "TRUE", "FALSE", None, "yes"                                    # valid/invalid
        ],
        "FILE_EXTENSION": [
            "'csv'", "NONE", None, "'csv.gz'", "", "ext!!"                              # valid/invalid
        ],
        "PARSE_HEADER": [
            True, False, "TRUE", "FALSE", None, "yes"                                    # valid/invalid
        ],
        "SKIP_HEADER": [
            0, 1, 10, -1, None, "5"                                                      # valid/invalid
        ],
        "SKIP_BLANK_LINES": [
            True, False, "TRUE", "FALSE", None, "yes"                                    # valid/invalid
        ],
        "DATE_FORMAT": [
            "'YYYY-MM-DD'", "AUTO", None, "", "invalid_format", "'MM/DD/YYYY'"          # valid/invalid
        ],
        "TIME_FORMAT": [
            "'HH24:MI:SS'", "AUTO", None, "", "bad", "'HH:MM'"                            # valid/invalid
        ],
        "TIMESTAMP_FORMAT": [
            "AUTO", "'YYYY-MM-DD HH24:MI:SS'", None, "", "bad"                            # valid/invalid
        ],
        "BINARY_FORMAT": [
            "HEX", "BASE64", "UTF8", None, "INVALID", ""                                 # valid/invalid
        ],
        "ESCAPE": [
            "'\\'", "NONE", "0x5C", None, "", "##"                                        # valid/invalid
        ],
        "ESCAPE_UNENCLOSED_FIELD": [
            "'\\'", "NONE", "0x5C", None, "", "!!"                                       # valid/invalid
        ],
        "TRIM_SPACE": [
            True, False, "TRUE", "FALSE", None, "yes"                                    # valid/invalid
        ],
        "FIELD_OPTIONALLY_ENCLOSED_BY": [
            "'\"'", "NONE", "0x22", None, "", "??"                                        # valid/invalid
        ],
        "NULL_IF": [
            ("'\\N'",), ("'NULL'", "''"), None, (), "", ("val1", "val2", ""), ("bad",)    # valid/invalid
        ],
        "ERROR_ON_COLUMN_COUNT_MISMATCH": [
            True, False, "TRUE", "FALSE", None, "yes"                                    # valid/invalid
        ],
        "REPLACE_INVALID_CHARACTERS": [
            True, False, "TRUE", "FALSE", None, "yes"                                    # valid/invalid
        ],
        "EMPTY_FIELD_AS_NULL": [
            True, False, "TRUE", "FALSE", None, "yes"                                    # valid/invalid
        ],
        "SKIP_BYTE_ORDER_MARK": [
            True, False, "TRUE", "FALSE", None, "yes"                                    # valid/invalid
        ],
        "ENCODING": [
            "'UTF8'", "'UTF16'", "'ISO88591'", None, "", "BAD_ENCODING"                  # valid/invalid
        ],
    },

    # ------------------------ formatTypeOptions: JSON ------------------------
    # (Only valid when TYPE = JSON)
    "JSON_OPTIONS": {
        "COMPRESSION": [
            "AUTO", "GZIP", "BZ2", "BROTLI", "ZSTD", "DEFLATE", "RAW_DEFLATE", "NONE",
            "ZIP", None, ""                                                # invalid variants
        ],
        "DATE_FORMAT": [
            "'YYYY-MM-DD'", "AUTO", None, "", "bad"                            # valid/invalid
        ],
        "TIME_FORMAT": [
            "'HH24:MI:SS'", "AUTO", None, "", "bad"
        ],
        "TIMESTAMP_FORMAT": [
            "AUTO", "'YYYY-MM-DD HH24:MI:SS'", None, "", "bad"
        ],
        "BINARY_FORMAT": [
            "HEX", "BASE64", "UTF8", None, "INVALID"
        ],
        "TRIM_SPACE": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "MULTI_LINE": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "NULL_IF": [
            ("'\\N'",), ("'NULL'", ""), None, (), ("bad",)
        ],
        "ENABLE_OCTAL": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "ALLOW_DUPLICATE": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "STRIP_OUTER_ARRAY": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "STRIP_NULL_VALUES": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "REPLACE_INVALID_CHARACTERS": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "IGNORE_UTF8_ERRORS": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "SKIP_BYTE_ORDER_MARK": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "ENCODING": [
            "'UTF8'", None, "", "BAD"
        ],
    },

    # ------------------------ formatTypeOptions: AVRO ------------------------
    "AVRO_OPTIONS": {
        "COMPRESSION": [
            "AUTO", "GZIP", "BROTLI", "ZSTD", "DEFLATE", "RAW_DEFLATE", "NONE",
            "ZIP", None, ""                                             # invalid
        ],
        "TRIM_SPACE": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "REPLACE_INVALID_CHARACTERS": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "NULL_IF": [
            ("'\\N'",), ("'NULL'", ""), None, (), ("bad",)
        ],
    },

    # ------------------------ formatTypeOptions: ORC ------------------------
    "ORC_OPTIONS": {
        "TRIM_SPACE": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "REPLACE_INVALID_CHARACTERS": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "NULL_IF": [
            ("'\\N'",), ("'NULL'", ""), None, (), ("bad",)
        ],
    },

    # ------------------------ formatTypeOptions: PARQUET ------------------------
    "PARQUET_OPTIONS": {
        "COMPRESSION": [
            "AUTO", "LZO", "SNAPPY", "NONE", "ZIP", None, ""               # valid/invalid
        ],
        "SNAPPY_COMPRESSION": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "BINARY_AS_TEXT": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "USE_LOGICAL_TYPE": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "TRIM_SPACE": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "USE_VECTORIZED_SCANNER": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "REPLACE_INVALID_CHARACTERS": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "NULL_IF": [
            ("'\\N'",), ("'NULL'", ""), None, (), ("bad",)
        ],
    },

    # ------------------------ formatTypeOptions: XML ------------------------
    "XML_OPTIONS": {
        "COMPRESSION": [
            "AUTO", "GZIP", "BZ2", "BROTLI", "ZSTD", "DEFLATE", "RAW_DEFLATE", "NONE",
            "ZIP", None, ""                                 # invalid
        ],
        "IGNORE_UTF8_ERRORS": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "PRESERVE_SPACE": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "STRIP_OUTER_ELEMENT": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "DISABLE_AUTO_CONVERT": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "REPLACE_INVALID_CHARACTERS": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "SKIP_BYTE_ORDER_MARK": [
            True, False, "TRUE", "FALSE", None, "yes"
        ],
        "NULL_IF": [
            ("'\\N'",), ("'NULL'", ""), None, (), ("bad",)
        ],
    },
}
