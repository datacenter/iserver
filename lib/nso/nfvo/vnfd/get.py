import time


class NfvoVnfdGet():
    def __init__(self):
        pass

    def is_vnfd(self, vnfd_id):
        vnfd = self.get_vnfd(vnfd_id)
        if vnfd is None:
            return False
        return True

    def get_vnfds_count(self):
        vnfds = self.get_vnfds()
        if vnfds is None:
            return 0
        return len(vnfds)

    def get_vnfds(self, output_format='json'):
        success = False
        response = None

        datastore = 'running'
        header = 'Accept'
        media_type = 'application/vnd.yang.collection'
        if self.nfvo_version == '3.x':
            if self.rest_handler.restconf_enabled:
                datapath = ('tailf-etsi-rel2-nfvo:nfvo', 'vnfd')
            else:
                datapath = ('nfvo', 'vnfd')

        if self.nfvo_version == '4.x':
            if self.rest_handler.restconf_enabled:
                datapath = ('etsi-nfv-descriptors:nfv', 'vnfd')
            else:
                datapath = ('nfv', 'vnfd')

        trace = 'nfvo.get_vnfds.%s' % (int(time.time() * 1000))
        success, response = self.rest_handler.get_data(
            output_format,
            datastore,
            datapath,
            header=header,
            media_type=media_type,
            params=None,
            trace=trace
        )

        if not success or response is None:
            self.log.error(
                'nso.get_vnfds',
                'Failure: %s' % (response)
            )
            return None

        if self.nfvo_version == '3.x':
            response = response['collection']['tailf-etsi-rel2-nfvo:vnfd']

        if self.nfvo_version == '4.x':
            response = response['collection']['etsi-nfv-descriptors:vnfd']

        return response

    def get_vnfd(self, vnfd_id, output_format='xml'):
        success = False
        response = None

        datastore = 'running'
        header = 'Accept'
        params = None

        if self.nfvo_version == '3.x':
            media_type = 'application/vnd.yang.data'
            if self.rest_handler.restconf_enabled:
                datapath = ('tailf-etsi-rel2-nfvo:nfvo', 'vnfd', vnfd_id)
            else:
                datapath = ('nfvo', 'vnfd', vnfd_id)

        if self.nfvo_version == '4.x':
            if self.rest_handler.restconf_enabled:
                media_type = 'application/vnd.yang.collection'
                datapath = ('etsi-nfv-descriptors:nfv', 'vnfd=%s' % (vnfd_id))
            else:
                media_type = 'application/vnd.yang.data'
                datapath = ('nfv', 'vnfd', vnfd_id)
                params = 'deep'

        trace = 'nfvo.get_vnfd.%s' % (int(time.time() * 1000))
        success, response = self.rest_handler.get_data(
            output_format,
            datastore,
            datapath,
            header=header,
            media_type=media_type,
            params=params,
            trace=trace
        )

        if not success or response is None:
            self.log.error(
                'nso.get_vnfd',
                'Failure: %s' % (response)
            )
            return None

        if self.nfvo_version == '3.x' and output_format == 'json':
            response = response['tailf-etsi-rel2-nfvo:vnfd']

        if self.nfvo_version == '4.x' and output_format == 'json':
            response = response['etsi-nfv-descriptors:vnfd']

        return response
