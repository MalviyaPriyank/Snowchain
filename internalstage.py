snowflake_internal_stage_param_test_cases = {
    # ------------------------ IDENTIFIER ------------------------
    "name": [
        "STAGE_INTERNAL",             # valid - standard
        "stage_data_lake",            # valid - lowercase
        '"My Stage"',                 # valid - quoted, contains space
        '"stage.test-01"',            # valid - quoted with special chars
        "123stage",                   # invalid - starts with number
        "stage-data",                 # invalid - special char without quotes
        "stage name",                 # invalid - space without quotes
        "",                           # invalid - empty
        "DB.SCHEMA.STAGE_INT",        # valid - fully qualified
        "DB.SCHEMA.SUB.STAGE",        # invalid - too many qualifiers
    ],

    # ------------------------ TEMP ------------------------
    "TEMP": [
        True, False,                  # valid
        "TEMP", "TEMPORARY",          # valid string
        None,                         # valid (optional)
        "PERMANENT",                  # invalid - not supported keyword
    ],

    # ------------------------ FILE FORMAT ------------------------
    "FILE_FORMAT": [
        {"FORMAT_NAME": "MY_CSV_FORMAT"},          # valid - named
        {"TYPE": "CSV"},                           # valid
        {"TYPE": "PARQUET"},                       # valid
        {"TYPE": "CUSTOM"},                        # valid
        {"TYPE": "JSON"},                          # valid
        {"FORMAT_NAME": "F1", "TYPE": "CSV"},      # invalid - mutually exclusive
        {"TYPE": "TXT"},                           # invalid - unsupported
        {},                                        # invalid - missing keys
    ],

    # ------------------------ ENCRYPTION ------------------------
    "ENCRYPTION": [
        {"TYPE": "SNOWFLAKE_FULL"},                # valid
        {"TYPE": "SNOWFLAKE_SSE"},                 # valid
        {"TYPE": "INVALID_TYPE"},                  # invalid
        {},                                        # valid - default encryption
        {"TYPE": ""},                              # invalid - empty
    ],

    # ------------------------ DIRECTORY TABLE ------------------------
    "DIRECTORY_TABLE": [
        {"ENABLE": True, "AUTO_REFRESH": False},   # valid
        {"ENABLE": False},                         # valid
        {"ENABLE": "TRUE"},                        # valid - string literal
        {"AUTO_REFRESH": "yes"},                   # invalid
        {},                                        # valid - defaults apply
    ],

    # ------------------------ COMMENT ------------------------
    "COMMENT": [
        "'Stage for raw data ingestion'",          # valid
        "'Temporary Snowpipe stage'",              # valid
        "''",                                      # valid
        None,                                      # valid
        "DROP TABLE; -- test",                     # invalid
        12345,                                     # invalid
    ],

    # ------------------------ TAG ------------------------
    "TAG": [
        {"env": "dev"},                            # valid
        {"project": "etl", "team": "data"},        # valid
        {"env": ""},                               # invalid
        {"@env": "prod"},                          # invalid
    ],
}
