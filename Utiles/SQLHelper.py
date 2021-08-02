from Config.DatabaseConfig import DatabaseConfig


class SQLHelper:
    def __init__(self):
        DB_CONFIG = DatabaseConfig.get_instance()
        self.mysql_connection_url = f"mysql://" \
                                    f"{DB_CONFIG.USER}:{DB_CONFIG.PASSWORD}" \
                                    f"@" \
                                    f"{DB_CONFIG.HOST}:{DB_CONFIG.PORT}" \
                                    f"/" \
                                    f"{DB_CONFIG.DB}"
