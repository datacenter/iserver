import time


class NfvoVnfdCreate():
    def __init__(self):
        pass

    def create_vnfd(self, vnfd_content, output_format='xml'):
        success = False
        response = None

        datastore = 'running'
        header = 'Content-Type'
        datapath = None
        if self.nfvo_version == '3.x':
            if self.restconf_enabled:
                datapath = ('tailf-etsi-rel2-nfvo:nfvo', )
            else:
                datapath = ('nfvo', )

        if self.nfvo_version == '4.x':
            if self.restconf_enabled:
                datapath = ('etsi-nfv-descriptors:nfv', )
            else:
                datapath = ('nfv', )

        if datapath is None:
            self.log.error(
                'nso.create_vnfd',
                'Unsupported nso instance'
            )
            return False

        trace = 'nfvo.create_vnfd.%s' % (int(time.time() * 1000))
        success, response = self.api_handler.set_data_value(
            output_format,
            datastore,
            datapath,
            vnfd_content,
            header=header,
            trace=trace
        )

        if not success:
            self.log.error(
                'nso.create_vnfd',
                'Failure: %s' % (response)
            )
            return False

        return True
