from lib import log_helper


class ProtocolNdInstance():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)

    def get_protocol_nd_instance(self, pod_id, node_id):
        managed_objects = None

        distinguished_name = 'topology/pod-%s/node-%s/sys/nd/inst' % (pod_id, node_id)
        managed_objects = self.get_managed_object(
            distinguished_name,
        )

        if managed_objects is None:
            return None

        if managed_objects['totalCount'] == '1':
            return managed_objects['imdata'][0]['ndInst']['attributes']

        return None

    def get_protocol_nd_instance_info(self, pod_id, node_id):
        managed_object = self.get_protocol_nd_instance(pod_id, node_id)

        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        if info['adminSt'] == 'enabled':
            info['enable'] = True
            info['__Output']['adminSt'] = 'Green'
        else:
            info['enable'] = False
            info['__Output']['adminSt'] = 'Red'

        return info
