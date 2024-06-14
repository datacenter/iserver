import os
import time
import json
import traceback
import yaml
import requests


class PsirtApi():
    def __init__(self, key, secret):
        self.api_key = key
        self.api_secret = secret
        self.api_token = None
        self.api_timeout_seconds = 3
        self.api_retries = 1
        self.ssl_verify = False

    def get_api_token(self):
        if self.api_token is not None:
            return self.api_token

        try:
            # curl -s -k -H "Content-Type: application/x-www-form-urlencoded" -X POST -d "client_id=deadbabebeef" -d "client_secret=deadbabebeef" -d "grant_type=client_credentials" https://id.cisco.com/oauth2/default/v1/token

            url = 'https://id.cisco.com/oauth2/default/v1/token'

            data = {}
            data['client_id'] = self.api_key
            data['client_secret'] = self.api_secret
            data['grant_type'] = 'client_credentials'

            response = requests.post(
                url,
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
                data=data,
                verify=self.ssl_verify
            )

            if response.status_code > 299:
                self.log.error(
                    'api.get_api_token',
                    'Failed to get api token: key [%s] secret [%s] code [%s]' % (
                        self.api_key,
                        self.api_secret,
                        response.status_code
                    )
                )
                self.log.error(
                    'api.get_api_token',
                    response.content
                )
                return None

            self.api_token = response.json()['access_token']

        except BaseException:
            self.log.error(
                'api.get_api_token',
                'Failed to get api token'
            )
            self.log.error('api.get_api_token', traceback.format_exc())
            return None

        return self.api_token
