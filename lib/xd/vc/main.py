from lib.vc import settings as vc_settings
from lib.xd.vc.cluster import VcCluster
from lib.xd.vc.dvs import VcDvs
from lib.xd.vc.host import VcHost
from lib.xd.vc.network import VcNetwork
from lib.xd.vc.vm import VcVm


class Vc(VcCluster, VcDvs, VcHost, VcNetwork, VcVm):
    def __init__(self):
        self.vc_instance = None

        VcCluster.__init__(self)
        VcDvs.__init__(self)
        VcHost.__init__(self)
        VcNetwork.__init__(self)
        VcVm.__init__(self)

    def load_pre_vc(self):
        if not self.load_pre_vc_instance():
            return False

        if not self.load_pre_vc_cluster():
            return False

        if not self.load_pre_vc_dvs():
            return False

        if not self.load_pre_vc_host():
            return False

        if not self.load_pre_vc_network():
            return False

        if not self.load_pre_vc_vm():
            return False

        return True

    def get_vc_names(self):
        names = []
        for key in self.vc_instance:
            names.append(key)
        return names

    def load_pre_vc_instance(self):
        self.vc_instance = self.get_pre_cache('vcenter', 'instance')
        if self.vc_instance is None:
            return False
        return True

    def set_post_vc_instance(self):
        return self.set_post_cache('vc-instance', self.vc_instance)

    def load_post_vc_instance(self):
        self.vc_instance = self.get_post_cache('vc-instance')
        if self.vc_instance is None:
            return False

        return True

    def prepare_vc_instances(self):
        vc_settings_handler = vc_settings.VcSettings(log_id=self.log_id)
        vc_instances = vc_settings_handler.get_vc_domain_instances(self.domain_name)
        if vc_instances is None:
            return False

        self.vc_instance = {}
        for vc_instance in vc_instances:
            self.vc_instance[vc_instance['name']] = vc_instance

            self.set_cache(
                'vcenter-%s-instance' % (vc_instance['name']),
                vc_instance
            )

        return True

    def get_vc_handlers(self):
        vc_settings_handler = vc_settings.VcSettings(log_id=self.log_id)
        vc_instances = vc_settings_handler.get_vc_domain_instances(self.domain_name)
        return vc_instances

    def prepare_vc(self, allow_partial=False):
        success = True

        self.my_output.debug('Get vcenter access...')
        if not self.prepare_vc_instances():
            self.my_output.error('Get vcenter instances failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get vcenter hosts...')
        if not self.prepare_vc_hosts():
            self.my_output.error('Get vcenter hosts failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get vcenter clusters...')
        if not self.prepare_vc_clusters():
            self.my_output.error('Get vcenter clusters failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get vcenter networks...')
        if not self.prepare_vc_networks():
            self.my_output.error('Get vcenter networks failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get vcenter dvs...')
        if not self.prepare_vc_dvs():
            self.my_output.error('Get vcenter dvs failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get vcenter vms...')
        if not self.prepare_vc_vms():
            self.my_output.error('Get vcenter vms failed')
            success = False
            if not allow_partial:
                return False

        return success

    def run_vc(self):
        self.my_output.debug('\t- host (independent)')
        if not self.run_vc_host_independent():
            return False

        self.my_output.debug('\t- net (independent)')
        if not self.run_vc_network_independent():
            return False

        self.my_output.debug('\t- vm')
        if not self.run_vc_vm():
            return False

        self.my_output.debug('\t- dvs')
        if not self.run_vc_dvs():
            return False

        self.my_output.debug('\t- net (xd)')
        if not self.run_vc_network_xd():
            return False

        self.my_output.debug('\t- host (xd)')
        if not self.run_vc_host_xd():
            return False

        self.my_output.debug('\t- cluster')
        if not self.run_vc_cluster():
            return False

        if not self.set_post_vc_instance():
            return False

        return True

    def run_vc_serial(self):
        return True

    def run_vc_mac(self):
        return True

    def load_post_vc(self):
        if not self.load_post_vc_instance():
            self.my_output.debug('VC instance failed')
            return False

        if not self.load_post_vc_cluster():
            self.my_output.debug('VC cluster failed')
            return False

        if not self.load_post_vc_dvs():
            self.my_output.debug('VC dvs failed')
            return False

        if not self.load_post_vc_host():
            self.my_output.debug('VC host failed')
            return False

        if not self.load_post_vc_network():
            self.my_output.debug('VC network failed')
            return False

        if not self.load_post_vc_vm():
            self.my_output.debug('VC vm failed')
            return False

        return True
