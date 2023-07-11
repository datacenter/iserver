class ProtocolBfdInstanceInfo():
    def __init__(self):
        self.bfd_instance = {}

    def get_protocol_bfd_instance_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            if key in ['healthInst']:
                continue

            info[key] = managed_object[key]

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        return info

    def get_protocol_bfd_instance(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bfd_instance:
            return self.bfd_instance[key]

        managed_object = self.get_protocol_bfd_instance_mo(pod_id, node_id)
        if managed_object is None or len(managed_object) == 0:
            return None

        self.bfd_instance[key] = self.get_protocol_bfd_instance_info(
            managed_object
        )

        self.log.apic_mo(
            'bfd.instance.info.%s' % (key),
            self.bfd_instance[key]
        )

        return self.bfd_instance[key]
