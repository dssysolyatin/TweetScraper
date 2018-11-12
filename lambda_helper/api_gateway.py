class ApiGateway:

    def query_parameter_from_event(self, event: dict, key: str, default = None):
        query_parameters = event.get('queryStringParameters')

        if query_parameters is None:
            return default

        return query_parameters.get(key, default)
