class K8sPodTemplateNginx():
    def __init__(self):
        pass

    def get_pod_template_nginx_body(self, params):
        body = self.get_pod_body_base(params)

        container_mo = {}
        container_mo['image'] = 'nginxinc/nginx-unprivileged'
        container_mo['name'] = 'nginx'

        body['spec']['containers'].append(container_mo)
        return body