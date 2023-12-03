from lib import log_helper

from lib.cvim import settings
from lib.openstack import main as openstack


class Cvim():
    def __init__(self, ocp_cluster_name, verbose=False, debug=False, log_id=None):
        self.log = log_helper.Log(log_id=log_id)
        self.verbose = verbose
        self.debug = debug
        self.log_id = log_id

        self.settings_handler = settings.CvimSettings(log_id=log_id)
        self.cvim_cluster_settings = self.settings_handler.get_cvim_cluster(ocp_cluster_name)
        if self.cvim_cluster_settings is None:
            raise ValueError('Cisco VIM cluster handler initialization failed')

        self.openstack_handler = openstack.Openstack(
            self.cvim_cluster_settings['openrc'],
            cluster_type='cvim',
            verbose=verbose,
            debug=debug,
            log_id=log_id
        )
