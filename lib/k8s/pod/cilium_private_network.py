import json
from lib import filter_helper


class K8sPodCiliumPrivateNetwork():
    def __init__(self):
        pass

    def get_pods_cilium_private_networks(self, cache_enabled=True):
        if not cache_enabled:
            self.get_pods(cache_enabled=False)

        agent = self.get_cilium_agent_pod_map(cache_enabled=True)
        all_pods = self.get_pods(cache_enabled=True)
        if all_pods is None:
            return None
        
        pods = []
        for pod in all_pods:
            if 'annotation' not in pod:
                continue

            if pod['annotation'] is None:
                continue

            if 'network.v1alpha1.isovalent.com/network-attachment' not in pod['annotation']:
                continue

            try:
                attachment = json.loads(pod['annotation']['network.v1alpha1.isovalent.com/network-attachment'])
            except BaseException:
                continue

            pod['private_network'] = {}
            pod['private_network']['name'] = attachment['network']
            pod['private_network']['ipv4'] = filter_helper.get(attachment, 'ipv4')
            pod['private_network']['ipv6'] = filter_helper.get(attachment, 'ipv6')
            pod['private_network']['mac'] = filter_helper.get(attachment, 'mac')
            if agent is None:
                pod['cilium_agent'] = None
            else:
                pod['cilium_agent'] = agent[pod['host_name']]

            pods.append(
                pod
            )

        return pods
