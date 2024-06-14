class ProtocolIsisTreeInfo():
    def __init__(self):
        self.isis_domain_trees = {}

    def get_protocol_isis_domain_tree_info(self, managed_object):
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

        if info['operSt'] == 'active':
            info['enable'] = True
            info['__Output']['operSt'] = 'Green'
        else:
            info['enable'] = False
            info['__Output']['operSt'] = 'Red'

        return info

    def get_protocol_isis_domain_trees_info(self, pod_id, node_id, instance_name, domain_name):
        key = '%s.%s.%s.%s' % (
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if key in self.isis_domain_trees:
            return self.isis_domain_trees[key]

        isis_domain_trees_mo = self.get_protocol_isis_domain_trees_mo(
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if isis_domain_trees_mo is not None:
            self.isis_domain_trees[key] = []
            for isis_domain_tree_mo in isis_domain_trees_mo:
                self.isis_domain_trees[key].append(
                    self.get_protocol_isis_domain_tree_info(
                        isis_domain_tree_mo
                    )
                )

        return self.isis_domain_trees[key]

    def get_protocol_isis_domain_trees(self, pod_id, node_id, instance_name, domain_name):
        trees = self.get_protocol_isis_domain_trees_info(pod_id, node_id, instance_name, domain_name)
        if trees is None:
            return None

        trees = sorted(
            trees,
            key=lambda i: int(i['id'])
        )

        return trees
