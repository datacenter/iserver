from lib import filter_helper


class ProtocolIsisDomainInfo():
    def __init__(self):
        self.isis_domains = {}

    def get_protocol_isis_domain_info(self, managed_object):
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

        # "dn": "topology/pod-1/node-201/sys/isis/inst-default/dom-overlay-1"
        info['instance'] = info['dn'].split('/')[5].split('-')[1]

        info['__Output']['name'] = 'Yellow'

        if info['operSt'] == 'ok':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        return info

    def get_protocol_isis_domains_info(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.isis_domains:
            return self.isis_domains[key]

        isis_domains_mo = self.get_protocol_isis_domains_mo(pod_id, node_id)
        if isis_domains_mo is not None:
            self.isis_domains[key] = []
            for isis_domain_mo in isis_domains_mo:
                self.isis_domains[key].append(
                    self.get_protocol_isis_domain_info(
                        isis_domain_mo
                    )
                )

        return self.isis_domains[key]

    def match_protocol_isis_domain(self, isis_domain_info, isis_domain_filter):
        if isis_domain_filter is None or len(isis_domain_filter) == 0:
            return True

        for ap_rule in isis_domain_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'name':
                if not filter_helper.match_string(value, isis_domain_info['name']):
                    return False

        return True

    def get_protocol_isis_domains(self, pod_id, node_id, isis_domain_filter=None, tunnel_info=False, lsp_info=False, interface_info=False, neighbor_info=False, tree_info=False, route_info=False):
        all_isis_domains = self.get_protocol_isis_domains_info(pod_id, node_id)
        if all_isis_domains is None:
            return None

        isis_domains = []

        for isis_domain_info in all_isis_domains:
            if not self.match_protocol_isis_domain(isis_domain_info, isis_domain_filter):
                continue

            if tunnel_info:
                isis_domain_info['tunnel'] = self.get_protocol_isis_domain_tunnels(
                    pod_id,
                    node_id,
                    isis_domain_info['instance'],
                    isis_domain_info['name']
                )

            if lsp_info:
                isis_domain_info['lsp'] = self.get_protocol_isis_domain_lsps(
                    pod_id,
                    node_id,
                    isis_domain_info['instance'],
                    isis_domain_info['name']
                )

            if interface_info:
                isis_domain_info['interface'] = self.get_protocol_isis_domain_interfaces(
                    pod_id,
                    node_id,
                    isis_domain_info['instance'],
                    isis_domain_info['name']
                )

            if neighbor_info:
                isis_domain_info['neighbor'] = self.get_protocol_isis_domain_neighbors(
                    pod_id,
                    node_id,
                    isis_domain_info['instance'],
                    isis_domain_info['name']
                )

            if tree_info:
                isis_domain_info['tree'] = self.get_protocol_isis_domain_trees(
                    pod_id,
                    node_id,
                    isis_domain_info['instance'],
                    isis_domain_info['name']
                )

            if route_info:
                isis_domain_info['route'] = self.get_protocol_isis_domain_routes(
                    pod_id,
                    node_id,
                    isis_domain_info['instance'],
                    isis_domain_info['name']
                )

            isis_domains.append(
                isis_domain_info
            )

        isis_domains = sorted(
            isis_domains,
            key=lambda i: i['name'].lower()
        )

        return isis_domains
