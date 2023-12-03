import time
from lib import xmltodict


class NfvoVnfiCreate():
    def __init__(self):
        pass

    def get_vnfi_name(self, vnfi_content):
        try:
            content = xmltodict.parse(vnfi_content, force_cdata=True)
            vnfi_name = content['vnf-info']['name']['#text']
        except BaseException:
            return None
        return vnfi_name

    def wait_for_vnfi_ready(self, vnfi_name, timeout=1800):
        start_time = int(time.time())
        while True:
            if self.is_vnfi_ready(vnfi_name, cache=False):
                return True

            time.sleep(15)
            if int(time.time()) - start_time > timeout:
                self.log.error(
                    'nso.wait_for_vnfi_ready',
                    'Timeout reached: %s' % (vnfi_name)
                )
                return False

    def wait_for_vnfi_defined(self, vnfi_name, timeout=30):
        start_time = int(time.time())
        while True:
            if self.is_vnfi(vnfi_name):
                return True

            time.sleep(5)
            if int(time.time()) - start_time > timeout:
                self.log.error(
                    'nso.wait_for_vnfi_defined',
                    'Timeout reached: %s' % (vnfi_name)
                )
                return False

    def create_vnfi(self, vnfi_content, output_format='xml', publish=False, trace=None):
        success = False
        response = None

        if self.nfvo_version == '3.x':
            return False, 'Unsupported NFVO 3.x version'

        if self.nfvo_version == '4.x' and not self.restconf_enabled:
            return False, 'REST API not supported for NFVO 4.x'

        success, response = self.api_handler.set_data_value(
            output_format,
            'running',
            ('etsi-nfv-descriptors:nfv',),
            vnfi_content,
            header='Content-Type',
            trace=trace
        )

        if not success:
            self.log.error(
                'nso.create_vnfi',
                'Failure: %s' % (response)
            )
            return False

        return True
