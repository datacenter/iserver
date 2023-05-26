import time
import json
import datetime
import traceback
import intersight

from lib import iaccount_helper


class IwoClient():
    def __init__(self, iaccount):
        self.iaccount = iaccount
        self.api_client = None
        self.iaccount_handler = iaccount_helper.IntersightAccount()

    def connect(self):
        if self.api_client is not None:
            return True

        iaccount_configuration = self.iaccount_handler.get_iaccount_configuration(
            self.iaccount
        )
        if iaccount_configuration is None:
            self.log.error(
                'iwo_client.connect',
                'iaccount not found: %s' % (self.iaccount)
            )
            return False

        start_time = int(time.time() * 1000)

        try:
            client_configured = True
            configuration = intersight.Configuration(
                host='https://%s' % (iaccount_configuration['server']),
                signing_info=intersight.HttpSigningConfiguration(
                    key_id=iaccount_configuration['keyid'],
                    private_key_path=iaccount_configuration['keyfile'],
                    signing_scheme=intersight.signing.SCHEME_RSA_SHA256,
                    signing_algorithm=intersight.signing.ALGORITHM_RSASSA_PKCS1v15,
                    hash_algorithm=intersight.signing.HASH_SHA256,
                    signed_headers=[intersight.signing.HEADER_REQUEST_TARGET,
                                    intersight.signing.HEADER_CREATED,
                                    intersight.signing.HEADER_EXPIRES,
                                    intersight.signing.HEADER_HOST,
                                    intersight.signing.HEADER_DATE,
                                    intersight.signing.HEADER_DIGEST,
                                    'Content-Type',
                                    'User-Agent'
                                    ],
                    signature_max_validity=datetime.timedelta(minutes=5)
                )
            )

            self.api_client = intersight.ApiClient(configuration)
            self.api_client.set_default_header('referer', 'https://%s' % (iaccount_configuration['server']))
            self.api_client.set_default_header('x-requested-with', 'XMLHttpRequest')
            self.api_client.set_default_header('Content-Type', 'application/json')
        except BaseException:
            client_configured = False
            self.log.error(
                'iwo_client.connect',
                traceback.format_exc()
            )

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.iwo(
            'connect',
            None,
            None,
            client_configured,
            duration_ms
        )

        return True

    def query(self, method, url, body=None, **kwargs):
        header = {}
        header['Accept'] = self.api_client.select_header_accept(['application/json'])
        header['Content-Type'] = self.api_client.select_header_content_type(['application/json'])
        auth_settings = ['cookieAuth', 'http_signature', 'oAuth2']
        query_parameters = []
        for key, value in kwargs.items():
            query_parameters.append((key, value))

        start_time = int(time.time() * 1000)

        try:
            success = True

            response = self.api_client.call_api(
                url,
                method,
                header_params=header,
                query_params=query_parameters,
                body=body,
                auth_settings=auth_settings,
                _return_http_data_only=True,
                _preload_content=False
            )

            output = []
            item_count = 0
            if response.data:
                output = json.loads(response.data)
                item_count = len(output)

        except Exception as exp:
            success = False
            output = None
            item_count = 0

            self.log.error(
                'iwo_client.query',
                traceback.format_exc()
            )

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time

        if body is None:
            self.log.iwo(
                method,
                url,
                None,
                success,
                duration_ms,
                item_count=item_count
            )
        else:
            self.log.iwo(
                method,
                url,
                json.dumps(body),
                success,
                duration_ms,
                item_count=item_count
            )

        return output

    def get(self, url, limit=500, **kwargs):
        if not self.connect():
            return None

        response = []
        cursor = 0
        while True:
            batch = self.query('GET', url, cursor=cursor, limit=500, **kwargs)
            if batch is None:
                break

            response = response + batch
            if len(batch) < limit:
                break

            cursor = cursor + limit

        return response

    def post(self, url, body=None, limit=500, **kwargs):
        if not self.connect():
            return None

        response = []
        cursor = 0
        while True:
            batch = self.query('POST', url, body=body, cursor=cursor, limit=500, **kwargs)
            if batch is None:
                break

            response = response + batch
            if len(batch) < limit:
                break

            cursor = cursor + limit

        return response

    def search(self, body, limit=500, **kwargs):
        if not self.connect():
            return None

        url = '/wo/api/v3/search'
        response = []
        cursor = 0
        while True:
            batch = self.query('POST', url, body=body, cursor=cursor, limit=500, **kwargs)
            if batch is None:
                break

            response = response + batch
            if len(batch) < limit:
                break

            cursor = cursor + limit

        return response
