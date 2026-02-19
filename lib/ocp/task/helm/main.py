import json
from lib import ssh


class OcpTaskHelm():
    def __init__(self):
        self.ocp_helm = None

    def get_helm_ssh_handler(self):
        management_ip = self.settings_handler.get_management_ip(self.ocp_cluster_settings['name'])
        if  management_ip is None:
            self.log.error('get_helm_ssh_handler', 'Management IP not found: %s' % (self.ocp_cluster_settings['name']))
            return None
        
        key_filename = self.settings_handler.get_management_ssh_pub_filename(self.ocp_cluster_settings['name'])
        if  key_filename is None:
            self.log.error('get_helm_ssh_handler', 'SSH public key not defined: %s' % (self.ocp_cluster_settings['name']))
            return None
        
        ssh_handler = ssh.Ssh(management_ip, 'core', key_filename=key_filename, log_id=self.log_id)
        success, exception_name, error = ssh_handler.is_ssh()
        if not success:
            self.log.error('get_helm_ssh_handler', error)
            return None

        success, output, error = ssh_handler.run_cmd('helm version')
        if not success:
            self.log.error('get_helm_ssh_handler', 'Helm not found on the management host: %s' % (management_ip))
            return None
        
        return ssh_handler

    def get_ocp_helm_mo(self, cache_enabled=True):
        if cache_enabled and self.ocp_helm is not None:
            return self.ocp_helm
        
        ssh_handler = self.get_helm_ssh_handler()
        if ssh_handler is None:
            return None
        
        success, output, error = ssh_handler.run_cmd('helm ls -A -o json')
        if not success:
            self.log.error('get_ocp_helm_mo', 'helm ls failed')
            return None
        
        try:
            content = json.loads(output)
        except BaseException:
            self.log.error('get_ocp_helm_mo', 'Failed to load json output')
            self.log.error('get_ocp_helm_mo', output)
            return None
        
        self.ocp_helm = content
        return self.ocp_helm
