from lib import ssh
from lib import output_helper


class OcpClusterConsole():
    def __init__(self, log_id=None):
        self.log_id = log_id
        self.my_output = output_helper.OutputHelper(
            log_id=log_id
        )

    def download_kubeadmin(self, installer_ip, installer_username, installer_password, silent=False):
        ssh_handler = ssh.Ssh(
            installer_ip,
            installer_username,
            password=installer_password,
            log_id=self.log_id
        )
        source = './install/auth/kubeadmin-password'
        destination = '/tmp/kubeadmin'
        success = ssh_handler.scp_file(
            source,
            destination,
            put=False
        )

        if not success:
            if not silent:
                self.my_output.error('Kubeadmin download failed')
            return None

        if not silent:
            self.my_output.default('Kubeadmin downloaded: %s => %s' % (source, destination))
        return destination
