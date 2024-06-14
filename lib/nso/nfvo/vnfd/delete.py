import time


class NfvoVnfdDelete():
    def __init__(self):
        pass

    def delete_vnfd(self, vnfd_id, output_format='json'):
        success = False
        response = None

        datastore = 'running'
        header = 'Accept'

        if self.nfvo_version == '3.x':
            if self.restconf_enabled:
                datapath = ('tailf-etsi-rel2-nfvo:nfvo', 'vnfd', vnfd_id)
            else:
                datapath = ('nfvo', 'vnfd', vnfd_id)

        if self.nfvo_version == '4.x':
            if self.restconf_enabled:
                datapath = ('etsi-nfv-descriptors:nfv', 'vnfd=%s' % (vnfd_id))
            else:
                datapath = ('nfv', 'vnfd', vnfd_id)

        trace = 'nfvo.delete_vnfd.%s' % (int(time.time() * 1000))
        success, response = self.api_handler.delete_path(
            output_format,
            datastore,
            datapath,
            header=header,
            trace=trace
        )

        if not success:
            self.log.error(
                'nso.delete_vnfd',
                'Failure: %s' % (response)
            )
            return False

        return True
