from lib import ip_helper


class ProtocolIsisTunnelInfo():
    def __init__(self):
        self.isis_domain_tunnels = {}

    def get_protocol_isis_domain_tunnel_info(self, managed_object):
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

        info['id_resolved'] = info['id']
        if ip_helper.is_valid_ipv4_address(info['id']):
            destination_node_info = self.get_node(
                node_ip=info['id']
            )
            if destination_node_info is not None:
                info['dest_node'] = destination_node_info['pod_node_name']
                info['id_resolved'] = '%s (%s)' % (
                    info['id'],
                    info['dest_node']
                )

        return info

    def get_protocol_isis_domain_tunnels_info(self, pod_id, node_id, instance_name, domain_name):
        key = '%s.%s.%s.%s' % (
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if key in self.isis_domain_tunnels:
            return self.isis_domain_tunnels[key]

        isis_domain_tunnels_mo = self.get_protocol_isis_domain_tunnels_mo(
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if isis_domain_tunnels_mo is not None:
            self.isis_domain_tunnels[key] = []
            for isis_domain_tunnel_mo in isis_domain_tunnels_mo:
                self.isis_domain_tunnels[key].append(
                    self.get_protocol_isis_domain_tunnel_info(
                        isis_domain_tunnel_mo
                    )
                )

        return self.isis_domain_tunnels[key]

    def get_protocol_isis_domain_tunnels(self, pod_id, node_id, instance_name, domain_name):
        tunnels = self.get_protocol_isis_domain_tunnels_info(pod_id, node_id, instance_name, domain_name)
        if tunnels is None:
            return None

        tunnels = sorted(
            tunnels,
            key=lambda i: i['id'].lower()
        )

        return tunnels
