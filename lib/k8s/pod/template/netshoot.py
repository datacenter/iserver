class K8sPodTemplateNetshoot():
    def __init__(self):
        pass

    def get_pod_template_netshoot_body(self, params):
        body = self.get_pod_body_base(params)

        container_mo = {}
        container_mo['command'] = ['sleep', 'infinite']
        container_mo['image'] = 'nicolaka/netshoot:latest'
        container_mo['securityContext'] = {}
        container_mo['securityContext']['runAsUser'] = 0
        container_mo['securityContext']['capabilities'] = {}
        container_mo['securityContext']['capabilities']['add'] = ['IPC_LOCK', 'SYS_RESOURCE', 'NET_RAW']
        container_mo['name'] = 'netshoot'

        body['spec']['containers'].append(container_mo)
        return body