from lib import log_helper

from lib.helm.chart.main import HelmChart
from lib.helm.release.main import HelmRelease
from lib import ssh


class Helm(
        HelmChart,
        HelmRelease
        ):
    def __init__(self, ip_address, username, password=None, key_filename=None, verbose=False, debug=False, log_id=None):
        HelmChart.__init__(self)
        HelmRelease.__init__(self)

        self.helm_ip = ip_address
        self.log = log_helper.Log(log_id=log_id)
        self.ssh_handler = ssh.Ssh(
            ip_address,
            username,
            password=password,
            key_filename=key_filename,
            verbose=verbose,
            debug=debug,
            log_id=log_id
        )
