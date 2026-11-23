class ProtocolIsisLspInfo():
    def __init__(self):
        self.isis_domain_lsps = {}

    def get_protocol_isis_domain_lsp_info(self, managed_object):
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

        return info

    def get_protocol_isis_domain_lsps_info(self, pod_id, node_id, instance_name, domain_name):
        key = '%s.%s.%s.%s' % (
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if key in self.isis_domain_lsps:
            return self.isis_domain_lsps[key]

        isis_domain_lsps_mo = self.get_protocol_isis_domain_lsps_mo(
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if isis_domain_lsps_mo is not None:
            self.isis_domain_lsps[key] = []
            for isis_domain_lsp_mo in isis_domain_lsps_mo:
                self.isis_domain_lsps[key].append(
                    self.get_protocol_isis_domain_lsp_info(
                        isis_domain_lsp_mo
                    )
                )

        return self.isis_domain_lsps[key]

    def get_protocol_isis_domain_lsps(self, pod_id, node_id, instance_name, domain_name):
        lsps = self.get_protocol_isis_domain_lsps_info(pod_id, node_id, instance_name, domain_name)
        if lsps is None:
            return None

        lsps = sorted(
            lsps,
            key=lambda i: i['sysId'].lower()
        )

        return lsps
