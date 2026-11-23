important fix in windows

C:\Users\<user>>\AppData\Local\Programs\Python\Python39\Lib\site-packages\kubevirt\api_client.py

    def __call_api(self, resource_path, method,
                   path_params=None, query_params=None, header_params=None,
                   body=None, post_params=None, files=None,
                   response_type=None, auth_settings=None, callback=None,
                   _return_http_data_only=None, collection_formats=None, _preload_content=True,
                   _request_timeout=None):

        config = Configuration()

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params,
                                                           collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params,
                                                    collection_formats)
            for k, v in path_params:
                # THIS NEEDS TO BE CHANGED
                resource_path = resource_path.replace(
                    '{%s}' % k, quote(str(v), safe=config.safe_chars_for_path_param))
                resource_path = resource_path.replace(
                    '{%s:[a-z0-9][a-z0-9\-]*}' % k, quote(str(v), safe=config.safe_chars_for_path_param))

C:\Users\<user>\AppData\Local\Programs\Python\Python39\Lib\site-packages\kubevirt\rest.py

    def PATCH(self, url, headers=None, query_params=None, post_params=None, body=None, _preload_content=True,
              _request_timeout=None):
        if headers['Content-Type'] == 'application/json-patch+json':
            headers['Content-Type'] = 'application/merge-patch+json'

        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)
