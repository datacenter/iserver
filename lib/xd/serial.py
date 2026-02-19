import copy


class Serial():
    def __init__(self):
        self.serial = None

    def get_serials(self):
        info = copy.deepcopy(self.serial)
        return info

    def set_post_serial(self):
        return self.set_post_cache('serial', self.serial)

    def load_post_serial(self):
        self.serial = self.get_post_cache('serial')
        if self.serial is None:
            return False

        return True

    def run_serial(self):
        self.serial = []

        self.my_output.debug('\t- cnc')
        if not self.run_cnc_serial():
            return False

        self.my_output.debug('\t- ucsm')
        if not self.run_ucsm_serial():
            return False

        self.my_output.debug('\t- fi')
        if not self.run_fi_serial():
            return False

        self.my_output.debug('\t- server')
        if not self.run_server_serial():
            return False

        self.my_output.debug('\t- nexus')
        if not self.run_nexus_serial():
            return False

        self.my_output.debug('\t- aci')
        if not self.run_aci_serial():
            return False

        self.my_output.debug('\t- vc')
        if not self.run_vc_serial():
            return False

        if not self.set_post_serial():
            return False

        return True
