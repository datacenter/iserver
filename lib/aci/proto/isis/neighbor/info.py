class ProtocolIsisNeighborInfo():
    def __init__(self):
        self.isis_domain_neighbors = {}

    def get_protocol_isis_domain_neighbor_info(self, managed_object):
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

        info['pod_node_name'] = '%s/%s' % (
            info['dn'].split('/')[1],
            self.get_node_name(
                info['dn'].split('/')[2].split('-')[1]
            )
        )
        info['instance'] = info['dn'].split('/')[5].split('-')[1]
        info['domain'] = info['dn'].split('/')[6].split('-')[1]
        info['interface'] = info['dn'].split('[')[1].split(']')[0]

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        return info

    def get_protocol_isis_domain_neighbors_info(self, pod_id, node_id, instance_name, domain_name):
        key = '%s.%s.%s.%s' % (
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if key in self.isis_domain_neighbors:
            return self.isis_domain_neighbors[key]

        isis_domain_neighbors_mo = self.get_protocol_isis_domain_neighbors_mo(
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if isis_domain_neighbors_mo is not None:
            self.isis_domain_neighbors[key] = []
            for isis_domain_neighbor_mo in isis_domain_neighbors_mo:
                self.isis_domain_neighbors[key].append(
                    self.get_protocol_isis_domain_neighbor_info(
                        isis_domain_neighbor_mo
                    )
                )

        return self.isis_domain_neighbors[key]

    def get_protocol_isis_domain_neighbors(self, pod_id, node_id, instance_name, domain_name):
        neighbors = self.get_protocol_isis_domain_neighbors_info(pod_id, node_id, instance_name, domain_name)
        if neighbors is None:
            return None

        neighbors = sorted(
            neighbors,
            key=lambda i: i['name'].lower()
        )

        return neighbors
