class Converter:
    @staticmethod
    def query_string_to_dict(query_string: str) -> dict:
        """
        parse query string to key value

        :param query_string: key=value&key2=value2

        :return: { key:value, key2:value2 }
        """
        query_string_result = {}
        query_array = query_string.split("&")

        for query in query_array:
            disassembled_query = query.split("=")
            try:
                key = disassembled_query[0]
                value = disassembled_query[1]
                query_string_result[key] = value
            except IndexError:
                pass

        return query_string_result
