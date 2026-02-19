class Mac():
    def __init__(self):
        self.mac = None

    def set_post_mac(self):
        return self.set_post_cache('mac', self.mac)

    def load_post_mac(self):
        self.mac = self.get_post_cache('mac')
        if self.mac is None:
            return False

        return True

    def run_mac(self):
        self.mac = []

        self.my_output.debug('\t- cnc')
        if not self.run_cnc_mac():
            return False

        self.my_output.debug('\t- ucsm')
        if not self.run_ucsm_mac():
            return False

        self.my_output.debug('\t- fi')
        if not self.run_fi_mac():
            return False

        self.my_output.debug('\t- server')
        if not self.run_server_mac():
            return False

        self.my_output.debug('\t- nexus')
        if not self.run_nexus_mac():
            return False

        self.my_output.debug('\t- aci')
        if not self.run_aci_mac():
            return False

        self.my_output.debug('\t- vc')
        if not self.run_vc_mac():
            return False

        if not self.set_post_mac():
            return False

        return True
