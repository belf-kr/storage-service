from sanic import Request


def get_query_string(request: Request):
    query_string_result = {}
    query_array = request.query_string.split("&")

    for query in query_array:
        disassembled_query = query.split("=")

        key = disassembled_query[0]
        value = disassembled_query[1]

        query_string_result[key] = value

    return query_string_result
