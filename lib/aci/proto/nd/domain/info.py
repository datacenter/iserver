class ProtocolNdDomainInfo():
    def __init__(self):
        pass

    def add_protocol_nd_domain_neighbor_info(self, domains, neighbors):
        for domain in domains:
            domain['neighborsCount'] = 0

        return domains

    def add_protocol_nd_domain_interface_info(self, domains, interfaces):
        for domain in domains:
            domain['interfacesCount'] = 0

            for interface in interfaces:
                if interface['domainName'] == domain['name']:
                    domain['interfacesCount'] = domain['interfacesCount'] + 1

        return domains

    def get_protocol_nd_domain_entry_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['__Output']['name'] = 'Yellow'

        (info['__Output']['health'], info['health']) = self.get_health_info(
            managed_object['healthInst']['cur']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_protocol_nd_domain_info(self, pod_id, node_id, nd_domain_name=None):
        managed_objects = self.get_protocol_nd_domain_mo(
            pod_id,
            node_id
        )

        info = []
        for managed_object in managed_objects:
            nd_domain_info = self.get_protocol_nd_domain_entry_info(
                managed_object
            )

            info.append(
                nd_domain_info
            )

        info = sorted(
            info,
            key=lambda i: i['name'].lower()
        )

        return info
