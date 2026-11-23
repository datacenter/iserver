import time
import requests
import traceback


class PsirtAdvisoryApi():
    def __init__(self):
        self.advisory_mo = None

    def get_advisory_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.advisory_mo is not None:
                return self.advisory_mo

            self.advisory_mo = self.get_psirt_cache_entry('advisory')
            if self.advisory_mo is not None:
                return self.advisory_mo

        api_handler = self.get_api_token()
        if api_handler is None:
            self.log.error(
                'api.get_advisory_mo',
                'No api token available'
            )
            return None

        try:
            start_time = int(time.time() * 1000)

            headers = {}
            headers['Authorization'] = 'Bearer %s' % (self.api_token)

            response = requests.get(
                'https://apix.cisco.com/security/advisories/v2/all',
                headers=headers
            )

            self.log.psirt(
                'get',
                'advisory',
                True,
                int(time.time() * 1000) - start_time
            )

            if response.status_code > 299:
                self.log.error(
                    'get_advisory_mo',
                    'Failed to get psirt advisory: %s' % (
                        headers
                    )
                )
                self.log.error(
                    'get_advisory_mo',
                    'Code [%s] Content [%s]' % (
                        response.status_code,
                        response.content
                    )
                )
                return None

            self.set_psirt_cache_entry(
                'advisory',
                response.json()['advisories']
            )

        except BaseException:
            self.log.error('psirt.get_advisory_mo', traceback.format_exc())
            self.log.psirt(
                'get',
                'advisory',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        return self.advisory_mo
