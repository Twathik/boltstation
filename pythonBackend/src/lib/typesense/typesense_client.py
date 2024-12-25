import typesense


typesense_client = typesense.Client(
    {
        "api_key": "xyz",
        "nodes": [{"host": "search.bolt.local", "port": "80", "protocol": "http"}],
        "connection_timeout_seconds": 2,
        "num_retries": 5,
        "log_level": "SILENT",
        "healthcheck_interval_seconds": 30,
    }
)
