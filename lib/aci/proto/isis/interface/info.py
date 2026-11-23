class ProtocolIsisInterfaceInfo():
    def __init__(self):
        self.isis_domain_interfaces = {}

    def get_protocol_isis_domain_interface_info(self, managed_object):
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
        info['instance'] = info['dn'].split('/')[5].split('-')[1]
        info['domain'] = info['dn'].split('/')[6].split('-')[1]

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        if info['iibState'] == 'Ready':
            info['__Output']['iibState'] = 'Green'
        else:
            info['__Output']['iibState'] = 'Red'

        return info

    def get_protocol_isis_domain_interfaces_info(self, pod_id, node_id, instance_name, domain_name):
        key = '%s.%s.%s.%s' % (
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if key in self.isis_domain_interfaces:
            return self.isis_domain_interfaces[key]

        isis_domain_interfaces_mo = self.get_protocol_isis_domain_interfaces_mo(
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if isis_domain_interfaces_mo is not None:
            self.isis_domain_interfaces[key] = []
            for isis_domain_interface_mo in isis_domain_interfaces_mo:
                self.isis_domain_interfaces[key].append(
                    self.get_protocol_isis_domain_interface_info(
                        isis_domain_interface_mo
                    )
                )

        return self.isis_domain_interfaces[key]

    def get_protocol_isis_domain_interfaces(self, pod_id, node_id, instance_name, domain_name):
        interfaces = self.get_protocol_isis_domain_interfaces_info(pod_id, node_id, instance_name, domain_name)
        if interfaces is None:
            return None

        interfaces = sorted(
            interfaces,
            key=lambda i: i['id'].lower()
        )

        return interfaces
