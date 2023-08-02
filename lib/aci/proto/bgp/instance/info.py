class ProtocolBgpInstanceInfo():
    def __init__(self):
        pass

    def get_protocol_bgp_instance_summary(self, instance_info):
        summary = {}
        summary['__Output'] = {}

        summary['domainsCount'] = len(instance_info['domain'])
        summary['domainsUp'] = 0
        for domain_info in instance_info['domain']:
            if domain_info['operSt'] == 'up':
                summary['domainsUp'] = summary['domainsUp'] + 1

        summary['domains'] = '%s/%s' % (
            summary['domainsUp'],
            summary['domainsCount']
        )
        if summary['domainsUp'] == summary['domainsCount']:
            summary['__Output']['domains'] = 'Green'
        else:
            summary['__Output']['domains'] = 'Red'

        summary['neighborsCount'] = len(instance_info['neighbor'])
        summary['neighborsUp'] = 0
        for neighbor_info in instance_info['neighbor']:
            if neighbor_info['state']['operSt'] == 'established':
                summary['neighborsUp'] = summary['neighborsUp'] + 1

        summary['neighbors'] = '%s/%s' % (
            summary['neighborsUp'],
            summary['neighborsCount']
        )
        if summary['neighborsUp'] == summary['neighborsCount']:
            summary['__Output']['neighbors'] = 'Green'
        else:
            summary['__Output']['neighbors'] = 'Red'

        return summary

    def get_protocol_bgp_instance_info(self, managed_object):
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
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

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

    def get_protocol_bgp_instance(self, pod_id, node_id):
        managed_object = self.get_protocol_bgp_instance_mo(pod_id, node_id)
        if managed_object is None or len(managed_object) == 0:
            return None

        return self.get_protocol_bgp_instance_info(managed_object)
