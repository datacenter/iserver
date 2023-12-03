class NfvoVnfiDelete():
    def __init__(self):
        pass

    def delete_vnfi(self, vnfi_name, output_format='json', trace=None):
        success = False
        response = None

        if self.nfvo_version == '3.x':
            return False, 'Unsupported NFVO 3.x version'

        if self.nfvo_version == '4.x' and not self.restconf_enabled:
            return False, 'REST API not supported for NFVO 4.x'

        success, response = self.api_handler.delete_path(
            output_format,
            'running',
            (
                'etsi-nfv-descriptors:nfv',
                'cisco-etsi-nfvo:vnf-info=%s' % (vnfi_name),
            ),
            header='Accept',
            trace=trace
        )

        if not success:
            self.log.error(
                'nso.delete_vnfi',
                'Failure: %s' % (response)
            )
            return False

        return True
