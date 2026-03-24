import json
from lib import filter_helper
from lib.k8s.pod.template.netshoot import K8sPodTemplateNetshoot
from lib.k8s.pod.template.nginx import K8sPodTemplateNginx

class K8sPodTemplate(
        K8sPodTemplateNetshoot,
        K8sPodTemplateNginx
    ):
    def __init__(self):
        K8sPodTemplateNetshoot.__init__(self)
        K8sPodTemplateNginx.__init__(self)

    def add_pod_body_udn_port(self, body, params):
        if 'udn-port' not in params or len(params['udn-port']) == 0:
            return body
        
        ports = []
        for item in params['udn-port']:
            if not isinstance(item, str):
                continue

            if len(item.split('/')) != 2:
                continue

            (protocol, port) = item.split('/')

            if protocol not in ['tcp', 'udp']:
                continue

            try:
                port = int(port)
            except BaseException:
                continue

            ports.append(
                dict(
                    protocol=protocol,
                    port=port
                )
            )

        if len(ports) == 0:
            return body

        if 'annotations' not in body['metadata']:
            body['metadata']['annotations'] = {}

        body['metadata']['annotations']['k8s.ovn.org/open-default-ports'] = json.dumps(ports)
        return body
    
    def get_pod_body_base(self, params):
        body = {}
        body['apiVersion'] = 'v1'
        body['kind'] = 'Pod'
        body['metadata'] = {}
        body['metadata']['namespace'] = params['namespace']
        body['metadata']['name'] = params['name']
        
        if params['label'] is not None and len(params['label']) > 0:
            body['metadata']['labels'] = params['label']

        if params['network'] is not None and len(params['network']) > 0:
            body['metadata']['annotations'] = {}
            body['metadata']['annotations']['k8s.v1.cni.cncf.io/networks'] = ','.join(params['network'])

        body['spec'] = {}
        body['spec']['containers'] = []
        if params['node'] is not None:
            body['spec']['nodeName'] = params['node']  

        body = self.add_pod_body_udn_port(body, params)
        return body

    def get_pod_template_body(self, params):
        app = filter_helper.get(params, 'app')
        if app is None:
            return None
        
        if app == 'netshoot':
            return self.get_pod_template_netshoot_body(params)

        if app == 'nginx':
            return self.get_pod_template_nginx_body(params)
                
        return None
    