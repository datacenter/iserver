import json
import traceback


class K8sCiliumConfigStatus():
    def __init__(self):
        pass

    def get_cilium_agents_status_mo(self, cache_enabled=True):
        pods = self.get_cilium_agent_pods(cache_enabled=cache_enabled)
        if pods is None:
            return None
        
        status_mo = []
        for pod in pods:
            agent_status_raw = self.get_pod_exec(
                self.cilium_namespace, 
                pod['name'], 
                'cilium status --verbose -o json'
            )
            if agent_status_raw is None:
                self.log.error('get_cilium_agents_status_mo', 'agent: %s' % (pod['name']))
                continue

            try:
                agent_status_mo = json.loads(
                    agent_status_raw.replace("'", '"').replace('None', 'null').replace('True', 'true').replace('False', 'false')
                )
            except BaseException:
                self.log.error('get_cilium_agents_status_mo', 'json cast on agent: %s' % (pod['name']))
                self.log.error('get_cilium_agents_status_mo', agent_status_raw)
                self.log.error('get_cilium_agents_status_mo', traceback.format_exc())
                continue

            agent_status_mo['metadata'] = {}
            agent_status_mo['metadata']['pod'] = pod['name']
            agent_status_mo['metadata']['node'] = pod['host_name']
            agent_status_mo['metadata']['ip'] = pod['pod_ip']
            status_mo.append(agent_status_mo)

        return status_mo
    