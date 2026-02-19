from lib.cnc import settings as cnc_settings
from lib.xd.cnc.node import CncNode


class Cnc(CncNode):
    def __init__(self):
        CncNode.__init__(self)

    def get_cnc_handlers(self):
        cnc_settings_handler = cnc_settings.CncSettings(log_id=self.log_id)
        cnc_controllers = cnc_settings_handler.get_cnc_domain_controllers(self.domain_name)
        return cnc_controllers

    def load_pre_cnc(self):
        if not self.load_pre_cnc_nodes():
            return False

        return True

    def prepare_cnc(self, allow_partial=False):
        success = True
        self.my_output.debug('Get cnc nodes...')
        if not self.prepare_cnc_nodes():
            self.my_output.error('Get cnc nodes failed')
            success = False
            if not allow_partial:
                return False

        return success

    def run_cnc(self):
        if not self.run_cnc_nodes():
            return False

        return True

    def run_cnc_serial(self):
        if not self.run_cnc_nodes_serial():
            return False

        return True

    def run_cnc_mac(self):
        if not self.run_cnc_nodes_mac():
            return False

        return True

    def load_post_cnc(self):
        if not self.load_post_cnc_nodes():
            return False

        return True
