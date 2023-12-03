import yaml

from lib import ssh


class OcpVmGetSsh():
    def __init__(self):
        pass

    def get_ocp_vm_ssh_handler(self, deployment):
        service_filename = deployment['deployment']['service']['ssh']
        yaml_content = deployment['files'][service_filename]
        content = yaml.safe_load(
            yaml_content
        )

        namespace = content['metadata']['namespace']
        name = content['metadata']['name']

        node_ip, node_port = self.k8s_handler.get_service_node_ip_port(
            namespace,
            name,
            cache_enabled=False
        )
        if node_ip is None or node_port is None:
            return None

        ssh_handler = ssh.Ssh(
            node_ip,
            deployment['ssh']['username'],
            port=node_port,
            password=deployment['ssh']['password'],
            endpoint_type=deployment['ssh']['type'],
            log_id=self.log_id
        )
        if ssh_handler is None:
            self.my_output.error(
                'Failed to initialize ssh session'
            )
        return ssh_handler

    def wait_ocp_vm_ssh_ready(self, deployment):
        self.my_output.default('Wait till virtual machine is ssh ready...')

        ssh_handler = self.get_ocp_vm_ssh_handler(deployment)
        if ssh_handler is None:
            return False

        self.my_output.default(
            'SSH check: (%s, %s) at %s:%s with timeout %s' % (
                ssh_handler.username,
                ssh_handler.password,
                ssh_handler.ip_address,
                ssh_handler.port,
                deployment['ready']['timeout']
            )
        )

        if not ssh_handler.wait_ssh(timeout=deployment['ready']['timeout']):
            self.my_output.error(
                'SSH check timed out'
            )
            return False

        self.my_output.default(
            'SSH works'
        )

        return True

    def wait_ocp_vm_ready(self, deployment):
        if not deployment['ready']['enabled']:
            return True

        if deployment['ready']['type'] not in ['ssh']:
            self.my_output.error(
                'Unsupported readiness type: %s' % (
                    deployment['ready']['type']
                )
            )
            return False

        if deployment['ready']['type'] == 'ssh':
            return self.wait_ocp_vm_ssh_ready(deployment)

        return True
