from lib import ssh


class OcpClusterManager():
    def __init__(self):
        pass

    def get_ocp_cluster_manager_info(self, validate=False):
        info = {}
        info['__Output'] = {}
        info['name'] = self.ocp_cluster_settings['name']
        info['installation'] = self.ocp_cluster_settings['parameters']['ocp']['installation']
        info['release'] = self.ocp_cluster_settings['parameters']['ocp']['release']
        info['cni'] = self.ocp_cluster_settings['parameters']['cni']['type']
        try:
            info['ssh'] = {}
            info['ssh']['ip'] = self.ocp_cluster_settings['parameters']['installer']['vm']['ip']
            info['ssh']['username'] = self.ocp_cluster_settings['parameters']['installer']['vm']['username']
            info['ssh']['password'] = self.ocp_cluster_settings['parameters']['installer']['vm']['password']
        except BaseException:
            info['ssh'] = None

        if validate and info['ssh'] is not None:
            ssh_handler = ssh.Ssh(
                info['ssh']['ip'],
                info['ssh']['username'],
                password=info['ssh']['password']
            )
            info['ssh']['validated'] = ssh_handler.is_ssh()
            if info['ssh']['validated']:
                info['ssh']['tick'] = '\u2713'
                info['__Output']['ssh.tick'] = 'Green'

        return info
